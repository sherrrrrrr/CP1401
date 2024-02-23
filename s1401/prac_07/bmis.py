"""
Pseudocode:
start program

define the_height with values [1.75, 1.5, 1.6, 1.7, 1.8, 1.9]
define the_weight with values [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72,
74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

for each height in the_height
    for each weight in the_weight
        set bmi to calculate_bmi(height, weight)
        set category to determine_weight_category(bmi)
        print "height (height)m, weight (weight)kg = bmi (bmi), considered (category)"
    end for each weight
end for each height

define function calculate_bmi(height, weight)
    return weight divided by (height squared)
end function

define function determine_weight_category(bmi)
    if bmi less than 18.5 then
        return "underweight"
    else if bmi less than 25 then
        return "normal"
    else if bmi less than 30 then
        return "overweight"
    else
        return "obese"
    end if
end function

define function get_valid_number(prompt, low, high)
    set number to user input converted to float
    while number less than low or number greater than high
        print "invalid input"
        set number to user input converted to float
    end while
    return number
end function

define function run_tests()
    print calculate_bmi(2, 60)
    print calculate_bmi(1.5, 100)
    print determine_weight_category(16.5)
    print determine_weight_category(25)
end function

if program is main then
    call main()
end if

end program
"""
def main():
    the_height = [1.75, 1.5, 1.6, 1.7, 1.8, 1.9]
    the_weight = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

    for height in the_height:
        for weight in the_weight:
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {category}")


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
    print(bmi)
    bmi = calculate_bmi(1.5, 100)
    print(bmi)

    category = determine_weight_category(16.5)
    print(category)
    category = determine_weight_category(25)
    print(category)


if __name__ == "__main__":
    main()
