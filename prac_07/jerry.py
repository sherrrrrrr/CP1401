"""
Pseudocode:
start program

prompt for speed_in_mph and convert to float
prompt for speed_limit_in_kph and convert to float

set speed_in_kph to convert_km_to_miles(speed_in_mph)
set fine to determine_fine(speed_in_kph, speed_limit_in_kph)

print fine amount

set bank_balance to 2000
subtract fine from bank_balance

print new bank_balance

define function convert_km_to_miles with kilometre as parameter
set conversion_rate to 0.621371
set miles to kilometre times conversion_rate
return miles

define function determine_fine with speed and speed_limit as parameters
define fine thresholds and amounts
calculate speed over the limit

end program
"""
def main():
    speed_in_mph = float(input("Please enter the speed in mph: "))
    speed_limit_in_kph = float(input("Please enter the speed limit in kph: "))

    speed_in_kph = convert_km_to_miles(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)

    print("You have to pay $", fine, "fine")

    bank_balance = 2000
    bank_balance -= fine

    print("After pay your fine, your current balance is $", bank_balance)

def convert_km_to_miles(kilometre):
    conversion_rate = 0.621371
    miles = kilometre * conversion_rate
    return miles

def determine_fine(speed, speed_limit):
    LEAST_LIMIT = 11
    LESS_LIMIT = 20
    HIGHER_LIMIT = 30
    HIGHEST_LIMIT = 40

    LEAST_LIMIT_FINE = 309
    LESS_LIMIT_FINE = 464
    MEDIUM_LIMIT_FINE = 696
    HIGHER_LIMIT_FINE = 1161
    HIGHEST_LIMIT_FINE = 1780

    SPEED_OVER_LIMIT = speed - speed_limit

    if speed_limit < LEAST_LIMIT:
        fine = LEAST_LIMIT_FINE
        demerit_points = 1
    elif LEAST_LIMIT <= speed_limit <= LESS_LIMIT:
        fine = LESS_LIMIT_FINE
        demerit_points = 3
    elif LESS_LIMIT < speed_limit <= HIGHER_LIMIT:
        fine = MEDIUM_LIMIT_FINE
        demerit_points = 4
    elif HIGHER_LIMIT < speed_limit <= HIGHEST_LIMIT:
        fine = HIGHER_LIMIT_FINE
        demerit_points = 6
    elif speed_limit > HIGHER_LIMIT:
        fine = HIGHEST_LIMIT_FINE
        demerit_points = 8

    return fine


if __name__ == "__main__":
    main()


