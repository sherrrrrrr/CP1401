"""1. Coffee Brew Ratio"""
def main():
    dose = get_valid_number("Dose: ")
    yield_value = get_valid_number("Yield: ")
    ratio = yield_value / dose
    coffee_style = determine_coffee_style(ratio)
    print(f"1:{ratio:.1f} is considered {coffee_style}")

def determine_coffee_style(ratio):
    """determines the coffee style based on the brew ratio."""
    if ratio <= 1:
        return "ristretto"
    elif ratio <= 2:
        return "normale"
    elif ratio <= 4:
        return "lungo"
    else:
        return "lungo"  # Anything above 1:4 is considered as lungo

def check_coffee():
    """tests the determine_coffee_style function with different ratios."""
    print("1:1 is considered", determine_coffee_style(1))    # ristretto
    print("1:2 is considered", determine_coffee_style(2))    # normale
    print("1:3.5 is considered", determine_coffee_style(3.5))  # lungo
    print("1:5 is considered", determine_coffee_style(5))    # lungo

def get_valid_number(prompt, max_value=100):
    """get the valid number from the user."""
    while True:
        try:
            number = float(input(prompt))
            if 0 < number <= max_value:
                return number
            print(f"Please enter a number greater than 0 and up to {max_value}.")
        except ValueError:
            print("Please enter a valid number.")

# uncomment to run the test function
# check_coffee()
main()
