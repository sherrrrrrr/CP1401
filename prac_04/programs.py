# 1.Error Checking
MIN_WORKER_LEVEL = 1
MAX_WORKER_LEVEL = 10
SALARY_PER_LEVEL = 5000


worker_level = int(input(f"Worker level ({MIN_WORKER_LEVEL}-{MAX_WORKER_LEVEL}): "))


while worker_level < MIN_WORKER_LEVEL or worker_level > MAX_WORKER_LEVEL:
    print("Invalid worker level")
    worker_level = int(input(f"Worker level ({MIN_WORKER_LEVEL}-{MAX_WORKER_LEVEL}): "))

salary = worker_level * SALARY_PER_LEVEL
print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")

# 2.Number Sequences
# a.
for number in range(1, 101, 2):
    print(number)
# b.
current_year = 2023
for year in range(1896, current_year + 1, 4):
    print(year, end=" ")
# c. write the even number between 50 and 100
for even_num in range(50, 101, 2):
    print(even_num, end=" ")

# 3.Menus
def display_menu():
    print("(S)miley")
    print("(F)rowny")
    print("(Q)uit")

def get_user_choice():
    return input("Enter your choice: ").upper()

def print_smiley_face():
    print(":-)")

def print_frowny_face():
    print(":-(")

while True:
    display_menu()
    choice = get_user_choice()

    if choice == 'S':
        print_smiley_face()
    elif choice == 'F':
        print_frowny_face()
    elif choice == 'Q':
        print("Farewell")
        break
    else:
        print("Invalid choice")

# 4. Accumulation
# Average Age
SENTINEL = -1
total_age = 0
num_people = 0

age = int(input("Enter age (or -1 to finish): "))
while age != SENTINEL:
    total_age += age
    num_people += 1
    age = int(input("Enter age (or -1 to finish): "))

if num_people > 0:
    average_age = total_age / num_people
    print(f"The average age of {num_people} people is: {average_age:.2f}")
else:
    print("No valid ages entered.")
# Smileys Count
smileys_count = 0
frownies_count = 0

while True:
    choice = input("(S)miley, (F)rowny, (Q)uit: ").upper()

    if choice == 'Q':
        break
    elif choice == 'S':
        print(":)")
        smileys_count += 1
    elif choice == 'F':
        print(":(")
        frownies_count += 1
    else:
        print("Invalid choice")

print(f"You printed {smileys_count} smileys and {frownies_count} frownies.")

# Total Numbers
total_numbers = 0

repetitions = int(input("How many numbers do you want to add up? "))
for i in range(repetitions):
    number = float(input(f"Enter number {i + 1}: "))
    total_numbers += number

print(f"The total of those {repetitions} numbers is: {total_numbers}")


# 5.Guessing Game
SECRET = 6
guess = int(input("Guess a number: "))
attempts = 1

while guess != SECRET:
    if guess < SECRET:
        print("Higher")
    else:
        print("Lower")

    guess = int(input("Guess a number: "))
    attempts += 1

print(f"You got it in {attempts} {'guess' if attempts == 1 else 'guesses'}!")


# 6. Nested Loops
rows = int(input("Rows: "))
columns = int(input("Columns: "))

for i in range(rows):
    for j in range(columns):
        print(j, end=" ")
    print()