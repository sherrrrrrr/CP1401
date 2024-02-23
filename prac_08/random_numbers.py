"""
Pseudocode:
start program

import random
function main()
    num_quantity = user input for "How many random numbers: "
    maximum = user input for "Maximum number: "
    numbers = empty list

    for _ in range(num_quantity)
        random_number = random integer from 0 to maximum
        add random_number to numbers

    display "The numbers are:" followed by numbers

    min_number = minimum value in numbers
    max_number = maximum value in numbers
    display "The minimum is" followed by min_number
    display "The maximum is" followed by max_number

    random_choice = randomly chosen value from numbers
    display "A randomly chosen number is" followed by random_choice

    reversed_numbers = reverse of numbers
    display "The numbers reversed are" followed by reversed_numbers

    sorted_numbers = sorted numbers
    display "The numbers sorted are" followed by sorted_numbers

end program
"""
import random

def main():
    num_quantity = int(input("How many random numbers: "))
    maximum = int(input("Maximum number: "))

    numbers = []
    for _ in range(num_quantity):
        numbers.append(random.randint(0, maximum))
    print("The numbers are:", numbers)

    min_number = min(numbers)
    max_number = max(numbers)
    print("The minimum is", min_number)
    print("The maximum is", max_number)

    random_choice = random.choice(numbers)
    print("A randomly chosen number is", random_choice)

    reversed_numbers = list(reversed(numbers))
    print("The numbers reversed are", reversed_numbers)

    sorted_numbers = sorted(numbers)
    print("The numbers sorted are", sorted_numbers)

main()