import random

class AnimalAccumulator:
    def __init__(self):
        self.animals = ["Antelope", "Fox", "Zebra"]  # Default list of animals
        self.total_income = 0
        self.days_simulated = 0

    def welcome_message(self):
        print("Welcome to the Animal Accumulator program!")
        print("Instructions: ...")  # Add instructions here

    def wait(self):
        lucky_number = random.randint(1, 100)
        print("Today's lucky number is", lucky_number)
        income_generated = 0
        for animal in self.animals:
            luck = random.randint(1, 100)
            if luck <= lucky_number:
                income_generated += len(animal)
            else:
                print(animal, "escaped!")
        self.total_income += income_generated
        self.days_simulated += 1
        print(f"After {self.days_simulated} days, total income is {self.total_income}")

    def display_animals(self):
        if self.animals:
            print("Animals in the collection:")
            for animal in self.animals:
                print(animal)
        else:
            print("No animals.")

    def add_new_animal(self):
        animal = input("Enter the name of the new animal: ").strip().title()
        if not animal.isalpha():
            print("Invalid animal name.")
            return
        if animal in self.animals:
            print(f"You already have {animal}")
            return
        cost = len(animal)
        if cost > self.total_income:
            print(f"You can't afford {animal}")
        else:
            self.animals.append(animal)
            print(f"Added {animal}.")
            self.total_income -= cost

    def quit_program(self):
        print("Final details:")
        print(f"Animals: {', '.join(sorted(self.animals)) if self.animals else 'No animals'}")
        print(f"Days simulated: {self.days_simulated}")
        print(f"Number of animals: {len(self.animals)}")
        print(f"Total income: {self.total_income}")
        save_choice = input("Do you want to save the animals to animals.txt? (y/n): ")
        if save_choice.lower() == 'y':
            with open("animals.txt", "w") as file:
                for animal in sorted(self.animals):
                    file.write(animal + "\n")
            print("Animals saved to animals.txt.")
        else:
            print("Animals not saved.")

    def start(self):
        self.welcome_message()
        load_choice = input("Would you like to load your animals from animals.txt (Y/n)? ")
        if load_choice.lower() == "y":
            self.load_animals_from_file()
        else:
            print("You start with these animals:")
            self.display_animals()

        while True:
            print(f"After {self.days_simulated} days, you have {len(self.animals)} animals and your total income is {self.total_income}")
            print("(W)ait\n(D)isplay animals\n(A)dd new animal\n(Q)uit")
            choice = input("Choose: ").lower()

            if choice == "w":
                self.wait()
            elif choice == "d":
                self.display_animals()
            elif choice == "a":
                self.add_new_animal()
            elif choice == "q":
                self.quit_program()
                break
            else:
                print("Invalid choice.")

    def load_animals_from_file(self):
        try:
            with open("animals.txt", "r") as file:
                self.animals = [line.strip() for line in file.readlines()]
            print("Animals loaded from animals.txt.")
        except FileNotFoundError:
            print("No animals.txt found. Starting with default animals.")

# Instantiate the program and start the main loop
animal_accumulator = AnimalAccumulator()
animal_accumulator.start()