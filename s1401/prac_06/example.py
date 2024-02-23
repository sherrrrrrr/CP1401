def main():
    height = get_valid_number("Height (m): ", 0, 3)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi:.1f}, which is considered {category}")



def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def run_tests():
    bmi = calculate_bmi(2, 60)
    print(bmi)  # This should be 15.0
    bmi = calculate_bmi(1.5, 100)
    print(bmi)  # This should be 44.4

    category = determine_weight_category(16.5)
    print(category)  # This should be underweight
    category = determine_weight_category(25)
    print(category)  # This should be overweight


if __name__ == "__main__":
    run_tests()

main()


