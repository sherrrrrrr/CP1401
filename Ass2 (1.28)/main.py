import random

# Constants
LOW_LUCK_THRESHOLD = 42

# Global variables
animals = []
total_income = 0
days_simulated = 0


def welcome():
    print("Welcome to the Animal Accumulator!")
    print("===================================")
    print("Instructions:")
    print("- Use the menu options to manage your animal collection.")
    print("- Each day, the luck value will determine the income generated.")
    print("- If luck is less than", LOW_LUCK_THRESHOLD, ", a random animal may escape.")
    print("===================================")


def load_animals():
    choice = input("Do you want to load animals from a file (y/n)? ")
    if choice.lower() == "y":
        filename = input("Enter the filename: ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    animal = line.strip()
                    animals.append(animal)
                animals.sort()
                print("Animals loaded successfully from", filename)
        except FileNotFoundError:
            print("File not found. Starting with three default animals.")
            animals.extend(["Lion", "Elephant", "Giraffe"])
    else:
        animals.extend(["Lion", "Elephant", "Giraffe"])
        print("Started with three default animals.")


def menu():
    print("\nMenu:")
    print("=====")
    print("(W)ait")
    print("(D)isplay animals")
    print("(A)dd new animal")
    print("(Q)uit")
    choice = input("Enter your choice: ").lower()
    return choice


def wait():
    global total_income
    global days_simulated

    luck = random.randint(0, 100)
    print("Luck:", luck)

    if luck < LOW_LUCK_THRESHOLD:
        if animals:
            escaped_animal = random.choice(animals)
            animals.remove(escaped_animal)
            print(escaped_animal, "escaped!")
        else:
            print("No animals left to escape.")

    income_generated = calculate_income(luck)
    total_income += income_generated

    days_simulated += 1
    print("Day", days_simulated, "ended.")
    print("Income generated:", income_generated)
    print("Total income:", total_income)


def calculate_income(luck):
    income_generated = 0
    for animal in animals:
        income = int(luck / 100 * len(animal))
        income_generated += income
    return income_generated


def display_animals():
    if animals:
        print("Animals:")
        print("=========")
        for animal in animals:
            print(animal)
    else:
        print("No animals.")


def add_animal():
    global total_income

    animal_name = input("Enter the name of the animal: ")
    if not animal_name:
        print("Animal name cannot be empty.")
        return

    animal_name = animal_name.title()

    if animal_name in animals:
        print("Animal already exists.")
        return

    cost = len(animal_name)
    if cost > total_income:
        print("Not enough income to add the animal.")
        return

    animals.append(animal_name)
    animals.sort()
    print(animal_name, "added successfully.")

    total_income -= cost
    print("Remaining income:", total_income)


def save_to_file():
    choice = input("Do you want to save the animals to a file (y/n)? ")
    if choice.lower() == "y":
        filename = "animals.txt"
        with open(filename, "w") as file:
            for animal in animals:
                file.write(animal + "\n")
        print("Animals saved successfully to", filename)


def end_program():
    print("===================================")
    print("Final Details:")
    print("==============")
    display_animals()
    print("Days simulated:", days_simulated)
    print("Number of animals:", len(animals))
    print("Total income:", total_income)

    save_to_file()


def animal_accumulator():
    welcome()
    load_animals()

    choice = menu()
    while choice != "q":
        if choice == "w":
            wait()
        elif choice == "d":
            display_animals()
        elif choice == "a":
            add_animal()

        choice = menu()

    end_program()


# Run the program
animal_accumulator()
