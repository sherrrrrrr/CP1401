"""
Pseudocode:
start program
function question_1
    display print_line
define print_line
    display ' "-" repeated 40 times'
end function

function question_2
    some_number = int(input("Number: "))
    if is_even with some_number
        display "{some_number} is even"
    else
        display "{some_number} is odd"
define is_even with number
    if number % 2 == 0
        return True
    else
        return False
end function

function question_3
    user_name = get_non_empty_string
    birth_place = get_non_empty_string
    display "Hi {user_name} from {birth_place}!"
define get_non_empty_string
    while True
        user_input = input("Enter a string: ")
        if user_input != ""
            return user_input
        else
            display "Input cannot be blank"
end function

function question_4
    minimum_number = int(input("Minimum number: "))
    maximum_number = int(input("Maximum number: "))

    while maximum_number <= minimum_number
        display "Your maximum must be greater than the minimum"
        maximum_number = int(input("Maximum number: "))
    number_list = list(range(minimum_number, maximum_number + 1))
    display "number_list"
end function

function question_5
    subject_list = []

    while True:
        subject_code = input("Enter subject code: ").strip().upper()

        if subject_code equal to ""
            break
        if valid_subject_list(subject_code)
            subject_list.append(subject_code)
        else
            display "Invalid subject code"

    call subject_list.sort
    display "You do these", length(subject_list), "subjects:"

    for subject_code in subject_list
        display "subject_code"
    if "CP1401" in subject_list
        display "You are cool"
    else:
        display "You are not cool"

define valid_subject_list(subject_code)
    if length(subject_code) not equal to 6
        return False
    if not subject_code[:2].isalpha() or not subject_code[2:].isdigit()
        return False
    return True
end function

end program
"""

def question_1():
    print_line()
def print_line():
    print("-" * 40)


def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_3():
    user_name = get_non_empty_string()
    birth_place = get_non_empty_string()
    print(f"Hi {user_name} from {birth_place}!")
def get_non_empty_string():
    while True:
        user_input = input("Enter a string: ")
        if user_input != "":
            return user_input
        else:
            print("Input cannot be blank")


def question_4():
    minimum_number = int(input("Minimum number: "))
    maximum_number = int(input("Maximum number: "))

    while maximum_number <= minimum_number:
        print("Your maximum must be greater than the minimum")
        maximum_number = int(input("Maximum number: "))
    number_list = list(range(minimum_number, maximum_number + 1))
    print(number_list)


def question_5():
    subject_list = []

    while True:
        subject_code = input("Enter subject code: ").strip().upper()

        if subject_code == "":
            break
        if valid_subject_list(subject_code):
            subject_list.append(subject_code)
        else:
            print("Invalid subject code")

    subject_list.sort()
    print("You do these {} subjects:".format(len(subject_list)))

    for subject_code in subject_list:
        print(subject_code)
    if "CP1401" in subject_list:
        print("You are cool")
    else:
        print("You are not cool")

def valid_subject_list(subject_code):
    if len(subject_code) != 6:
        return False
    if not subject_code[:2].isalpha() or not subject_code[2:].isdigit():
        return False
    return True



question_1()
question_2()
question_3()
question_4()
question_5()
