import random
print("Welcome to the Animal Accumulator.")
print("Animals cost and generate income according to their name length (e.g., a Zebra costs 5).")
print("Each day, animals generate income based on luck. Sometimes they escape.")
print("You can buy new animals with the income your animals generates.")
choice = input("Would you like to load your animals from animals.txt (Y/n)? ")
animals = []

def display_animals():
    if len(animals) == 0:
        print("There are no animals in the collection.")
    else:
        print("Animals in the collection:")
        for animal in animals:
            print(animal)

def add_animal():
    animal = input("Enter the name of the animal: ")
    animals.append(animal)
    print(animal, "has been added to the collection.")

def remove_animal():
    if len(animals) == 0:
        print("There are no animals in the collection to remove.")
    else:
        animal = input("Enter the name of the animal to remove: ")
        if animal in animals:
            animals.remove(animal)
            print(animal, "has been removed from the collection.")
        else:
            print(animal, "is not in the collection.")

def random_animal():
    if len(animals) == 0:
        print("There are no animals in the collection.")
    else:
        random_animal = random.choice(animals)
        print("A random animal from the collection is:", random_animal)

def main():
    while True:
        print()
        print("===== Animal Accumulator =====")
        print("1. Display animals")
        print("2. Add an animal")
        print("3. Remove an animal")
        print("4. Get a random animal")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_animals()
        elif choice == "2":
            add_animal()
        elif choice == "3":
            remove_animal()
        elif choice == "4":
            random_animal()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()