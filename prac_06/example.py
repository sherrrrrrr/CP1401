def main():
    number_of_people = int(input("Enter the number of people: "))

    with open("bmis.txt", "w") as file:
        for _ in range(number_of_people):
            height = get_valid_number("Enter the height (m): ", 0, float("inf"))
            weight = get_valid_number("Enter the weight (kg): ", 0, float("inf"))
            bmi = calculate_bmi(height, weight)
            file.write(f"{bmi:.1f}\n")

    print("BMI values have been written to bmis.txt")

    with open("bmis.txt", "r") as file:
        for line in file:
            bmi = float(line.strip())
            category = determine_weight_category(bmi)
            print(f"BMI {bmi:.1f}, considered {category}")


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


if __name__ == "__main__":
    main()
