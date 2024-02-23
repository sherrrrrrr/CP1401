"""
Pseudocode:
start program
function print_menu
    display "Please choose from:"
    for each coffee in coffee_menu
        display "coffee"
define coffee_menu dictionary to store different coffee types and
 their respective preparation steps
function get_valid_coffee_order
    while True
        get order from user and capitalize it
        if order in coffee_menu
            return order
        else
            display "Invalid order"
function make_coffee(order)
    display "Here's how to make a {order}:"
    for each step in coffee_menu with order
        display "-" + step
function main
    display "Welcome to the IT@JCU Coffee Shop"
    display "(O)rder - (D)rink - (R)andom choice - (Q)uit"
    get choice
    while choice is not 'Q'
        choice equal input(">>> ").upper()
        if choice is 'O'
            display menu
            set order to result of get_valid_coffee_order
            make_coffee with order
        elif choice is 'D'
            display "Oh... where's my coffee?"
        elif choice is 'R'
            set order to a random choice from coffee_menu keys
            make_coffee with order
        elif choice is 'Q'
            display "Thanks for drinking coffee"
        else:
            display "Invalid option"
        display menu "(O)rder - (D)rink - (R)andom choice - (Q)uit"
call the main function
end program
"""
import random
def print_menu():
    print("Please choose from:")
    for coffee in coffee_menu:
        print(coffee)

coffee_menu = {
    "Flat White": [
        "Insert portafilter into grinder",
        "Press grind button to grind beans into portafilter",
        "Distribute grounds",
        "Tamp grounds",
        "Insert full portafilter into group head",
        "Press shot button to pour espresso into cup",
        "Fill jug with milk",
        "Steam milk until nice microfoam formed and milk up to temperature",
        "Swirl milk gently in jug",
        "Pour milk into cup... carefully, artistically :)"
    ],
    "Espresso": [
        "Insert portafilter into grinder",
        "Press grind button to grind beans into portafilter",
        "Distribute grounds",
        "Tamp grounds",
        "Insert full portafilter into group head",
        "Press shot button to pour espresso into cup"
    ],
    "Long Black": [
        "Insert portafilter into grinder",
        "Press grind button to grind beans into portafilter",
        "Distribute grounds",
        "Tamp grounds",
        "Insert full portafilter into group head",
        "Press shot button to pour espresso into cup",
        "Add hot water to cup"
    ],
    "Babyccino": [
        "Add warm milk to a small cup",
        "Sprinkle chocolate powder on top"
    ],
    "Cappuccino": [
        "Insert portafilter into grinder",
        "Press grind button to grind beans into portafilter",
        "Distribute grounds",
        "Tamp grounds",
        "Insert full portafilter into group head",
        "Press shot button to pour espresso into cup",
        "Fill jug with milk",
        "Steam milk until nice microfoam formed and milk up to temperature",
        "Swirl milk gently in jug",
        "Pour milk into cup, leaving room for froth",
        "Add froth on top"
    ]
}

def get_valid_coffee_order():
    while True:
        order = input("? ").capitalize()
        if order in coffee_menu:
            return order
        else:
            print("Invalid order")

def make_coffee(order):
    print(f"Here's how to make a {order}:")
    for step in coffee_menu[order]:
        print(f"- {step}")

def main():
    print("Welcome to the IT@JCU Coffee Shop")
    print("(O)rder - (D)rink - (R)andom choice - (Q)uit")
    choice = ''
    while choice != 'Q':
        choice = input(">>> ").upper()
        if choice == 'O':
            print_menu()
            order = get_valid_coffee_order()
            make_coffee(order)
        elif choice == 'D':
            print("Oh... where's my coffee?")
        elif choice == 'R':
            order = random.choice(list(coffee_menu.keys()))
            make_coffee(order)
        elif choice == 'Q':
            print("Thanks for drinking coffee")
        else:
            print("Invalid option")
        print("(O)rder - (D)rink - (R)andom choice - (Q)uit")


if __name__ == "__main__":
    main()