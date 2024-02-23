"""CP1401 - Practical 7 - Debugging.
The "demo" problem shows how the answers should be written.
Follow the example and template to answer the questions (find and fix problems) below.
"""

def demo():
    """Problematically do list duplication and reversing."""
    things = [1, 2, 3, 4]
    new_things = dupli_reversify(things)
    print(new_things)
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x + x.reverse()

# Problem(s) for demo program:
# x.reverse() modifies the list in-place and evaluates to None (it does not evaluate to a list).
# x (list) + None gives a TypeError
# (Notice that the answer is about the bug/problem, not about style, names, formatting, etc.)

# Fixed code for demo program:
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x[:] + x[::-1]
    # or
    # return x + list(reversed(x))
# (Notice that the answer includes the whole fixed function. No style/naming issues have been improved.)


# Questions start here:

# def main_1():
#    """Determine the parity of a user's number."""
#    number = int(input("Enter number: "))
#    parity = calculate_parity
#    print(parity)


def calculate_parity(number):
    """Calculate the parity (0 or 1) of number passed in."""
    return (number%2)

# Problem(s) for program 1:
# the 'calculate_parity' function not called with 'number'

# Fixed code for program 1:
def main_1():
    number = int(input("Enter number: "))
    parity = calculate_parity(number)
    print(parity)



# def main_2():
#    """Print numbers from 0 up to the user's input multiplied by 2."""
#    # E.g., if input is 13, should print 0 2 4 6 8 10 12 14 16 18 20 22 24 26
#    numnums = input("How many: ")
#    for i in numnums:
#        print(i * 2)

# Problem(s) for program 2:
# The input is not converted to an integer

# Fixed code for program 2:
def main_2():
    numnums = int(input("How many: "))
    for i in range(numnums + 1):
        print(i * 2)


# def main_3():
#    length, width = 12, 10
#    area = calculate_area(length, width)
#    print(f"The area is {area}")

# def calculate_area(l, w):
#    """Calculate the area of a rectangle from its dimensions."""
#    result = l * w
#    print(result)

# Problem(s) for program 3:
# 'calculate_area' function have to return the area, not print result.

# Fixed code for program 3:
def main_3():
    length, width = 12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(l, w):
    return l * w  # Return the area


# def main_4():
#    """Show how old a person will be in the future."""
#    increment = 10
#    age = int(input("Age: "))
#    while age < 0 and age > 120:
#        print("Invalid age")
#        age = int(input("Age: "))
#    print(f"In {increment} years, you will be {age} years old!")

# Problem(s) for program 4:
# the while loop condition is incorrect.
# 'and' operator should be 'or'.
# the age can not update before print.

# Fixed code for program 4:
def main_4():
    increment = 10
    age = int(input("Age: "))
    while age < 0 or age > 120:  # Use 'or' to check the age range
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {age + increment} years old!")


# main_1()
# main_2()
# main_3()
main_4()
