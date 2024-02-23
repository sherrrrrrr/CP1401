#1. Tax
TAX_RATE_LESS = 0.02  # 2%
TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%

TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_LESS = 500
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

if income < TAX_THRESHOLD_LOW:
    total_tax = 0
    take_home_pay = income

elif TAX_THRESHOLD_LOW <= income <= TAX_THRESHOLD_LESS:
    total_tax = income * TAX_RATE_LESS
    take_home_pay = income - total_tax

elif TAX_THRESHOLD_LESS < income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
    take_home_pay = income - total_tax

elif TAX_THRESHOLD_HIGH < income:
    total_tax = income * TAX_RATE_HIGH
    take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")
# TODO: complete this part of the program here


#2. Car Insurance

YOUTH_AGE = 18
ADULT_AGE = 25
age = float(input("The applicant's age: "))

if age < YOUTH_AGE:
    print("Applicant is refused hire altogether.")

elif YOUTH_AGE <= age <= ADULT_AGE:
    print("Applicant is required to purchase special insurance.")

elif ADULT_AGE < age:
    print("Applicant is not required to purchase insurance.")


#3. Simple Password Checker
password = float(input("Enter your password: "))
secret_password = 13960522
if password == secret_password:
    print("Access granted")

else:
    print("Access denied.")


#4. Dog Years
DOG_EARLY_AGE = 10.5
DOG_BEHIND_AGE = 4
HUMAN_EARLY_YEAR = 2

human_year = float(input("Age in human years: "))
if human_year <= HUMAN_EARLY_YEAR:
    dog_year = human_year * DOG_EARLY_AGE
else:
    dog_year = (HUMAN_EARLY_YEAR * DOG_EARLY_AGE) + (human_year- HUMAN_EARLY_YEAR) * DOG_BEHIND_AGE
    print("Age in dog years is ", dog_year, sep="")


#5. Rock of Ages
user_age = float(input("Enter your age: "))
if user_age < 0 or user_age > 120:
    print("Invalid age.")
elif 0 < user_age < 18:
    print("Enjoy your time.")
elif 18 <= user_age <= 25:
    print("You have to study hard.")
elif 25 < user_age <= 40:
    print("You have to swork hard.")
elif 40 < user_age <= 80:
    print("You have to take your health.")
elif 80 < user_age < 120:
    print("I wish you spend a good time with your family.")


#6. Speeding Fines
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
