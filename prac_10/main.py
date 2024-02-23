import random

COFFEE_MENU = {
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


def print_menu():
    print("Please choose from:")
    for coffee in COFFEE_MENU:
        print(coffee)


def get_valid_coffee_order():
    while True:
        order = input("? ").capitalize()
        if order in COFFEE_MENU:
            return order
        else:
            print("Invalid order")


def make_coffee(order):
    print(f"Here's how to make a/n {order}:")
    for step in COFFEE_MENU[order]:
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
            order = random.choice(list(COFFEE_MENU.keys()))
            make_coffee(order)
        elif choice == 'Q':
            print("Thanks for drinking coffee")
        else:
            print("Invalid option")
        print("(O)rder - (D)rink - (R)andom choice - (Q)uit")


main()
