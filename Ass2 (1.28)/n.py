import random

animals = ["Antelope","Fox","Zebra"]
income = 0

def display_animals():
    print("Animals in the collection:")
    for animal in animals:
        print(animal)

def add_animal():
    animal = self.get_valid_animal()
    if animal is None:
        return

    if animal in self.animals:
        print(f"You already have {animal}")
        return

    cost = len(animal) * 5
    if cost > income:
        print("You can't afford", animal)
    else:
        animals.append(animal)
        print("Added", animal + ".")
        update_income(-cost)

def wait():
    lucky_number = random.randint(1, 100)
    print("Today's lucky number is", lucky_number)
    income_generated = 0
    for animal in animals:
        luck = random.randint(1, 100)
        if luck <= lucky_number:
            animal_income = len(animal)
            income_generated += animal_income
            print(f"{animal} earned {animal_income},", end=" ")
        else:
            print(animal, "escaped!")
    print()  # New line after displaying earnings
    update_income(income_generated

def update_income(amount):
    global income
    income += amount

def main():
    print("Welcome to the Animal Accumulator.")
    print("Animals cost and generate income according to their name length (e.g., a Zebra costs 5).")
    print("Each day, animals generate income based on luck. Sometimes they escape.")
    load_choice = input("Would you like to load your animals from animals.txt (Y/n)? ")
    if load_choice.lower() == "y":
        load_animals_from_file()
    else:
        print("You start with these animals:")
        display_animals()

    day = 0
    while True:
        print("After", day, "days, you have", len(animals), "animals and your total income is", income)
        print("(W)ait\n(D)isplay animals\n(A)dd new animal\n(Q)uit")
        choice = input("Choose: ").lower()

        if choice == "w":
            wait()
            day += 1
        elif choice == "d":
            display_animals()
        elif choice == "a":
            add_animal()
        elif choice == "q":
            break
        else:
            print("Invalid choice.")

    print("You finished with no animals.")

main()
