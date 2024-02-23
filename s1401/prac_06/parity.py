"""2. parity"""
def main():
    # test print_parity function
    print_parity(4)
    print_parity(41)

    # test is_odd function
    print(f"Is 4 odd? Expected False: {is_odd(4)}")
    print(f"Is 41 odd? Expected True: {is_odd(41)}")
# run the main function, test all functions

def print_parity(number):
    """print the parity of a number passed into it (parameter)."""
    parity = number % 2
    print(f"Parity of {number} should be {parity}: {parity}")

def determine_parity(number):
    """determines the parity of a given number, return to the function. """
    return number % 2

def is_odd(number):
    """if the number is odd number, return true, if the number is not odd number, return false."""
    return number % 2 == 1

if __name__ == "__main__":
    main()
