MAXMIUM_AGE = 150
MINMIUM_AGE = 0

def main():
    age = validate_age()
    message = determine_age(age)

    print((f"At {age} years old, you are: {message}"))


def determine_age(age):
    if age < 18:
        message = "child"
    elif age < 65:
        message = "adult"
    else:
        message = "geriatric"
    return message


def validate_age():
    age = int(input("age: "))
    while age < MINMIUM_AGE or age > MAXMIUM_AGE:
        print("Invalid age")
        age = int(input("age: "))
    return age


main()


