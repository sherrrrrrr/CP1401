import random

def main():
    animals = load_animals()
    income = 0
    days = 0
    while True:
        display_menu()
        choice = input("Choose: ").upper()
        if choice == "W":
            luck, income, animals = simulate_day(luck, income, animals)
            days += 1
        elif choice == "D":
            display_animals(animals)
        elif choice == "A":
            animals, income = add_animal(animals, income)
        elif choice == "Q":
            if save_animals(animals