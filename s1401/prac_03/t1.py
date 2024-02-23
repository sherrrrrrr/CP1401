LEAST_LIMIT = 11
LESS_LIMIT = 20
HIGHER_LIMIT = 30
HIGHEST_LIMIT = 40

LEAST_LIMIT_FINE = 309
LESS_LIMIT_FINE = 464
MEDIUM_LIMIT_FINE = 696
HIGHER_LIMIT_FINE = 1161
HIGHEST_LIMIT_FINE = 1780

speed = int(input("Please enter your speed (km/h): "))
speed_limit = int(input("please enter the speed limit (km/h): "))
SPEED_OVER_LIMIT = speed - speed_limit
speed_over_limit = speed - speed_limit

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

print("You have over speed for", speed_over_limit, "km/h")
print ("You should pay", fine, "dollars")
print("Your demerit points is ", demerit_points, sep="")