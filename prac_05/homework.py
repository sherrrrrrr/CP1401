# 1. Percentage change
original = float(input("Enter your original value: "))
change = float(input("Enter percentage change(positive for increase, negative for decrease): "))
result = original + (original * change)
print(f"Original:{original},Change:{change},Result:{result}")


# 2. Time of day
time_of_day = int(input("Enter the time of the day (you can only choose your time from 0-23): "))
coming_or_going =input("Are you coming or going? ")
if time_of_day < 12:
    datetime = "before noon"
else:
    datetime = "after noon"

print(f"It is {datetime} and you are {coming_or_going.lower()}."
      f"{'Hi!' if coming_or_going.lower() == 'coming' else 'Bye!'}")


# 3. Coffee orders
coffee_type = input("Would you like black or white coffee? ").lower()
coffee_size = input("What size would you like? (small, medium, or large) ").lower()

black_small_price = 3
black_medium_price = 4
black_large_price = 5

white_small_price = black_small_price + 1
white_medium_price = black_medium_price + 1
white_large_price = black_large_price + 1

if coffee_type != "white" and coffee_type != "black":
    coffee_type = "black"

if coffee_size != "small" and coffee_size != "medium" and coffee_size != "large":
    coffee_size = "large"


if coffee_type == "black":
    if coffee_size == "small":
        final_price = black_small_price
    elif coffee_size == "medium":
        final_price = black_medium_price
    elif coffee_size == "large":
        final_price = black_large_price
else:
    if coffee_size == "small":
        final_price = white_small_price
    elif coffee_size == "medium":
        final_price = white_medium_price
    elif coffee_size == "large":
        final_price = white_large_price

print("Your total cost is $" + str(final_price))


# 4. Coffee orders with error-checking
coffee_type = input("Would you like black or white coffee? ").lower()
if coffee_type == "black" or coffee_type == "white":
    coffee_size = input("What size would you like? (small, medium, large) ").lower()
    if coffee_size == "small" or coffee_size == "medium" or coffee_size == "large":
        black_small_price = 3
        black_medium_price = 4
        black_large_price = 5

        white_small_price = black_small_price + 1
        white_medium_price = black_medium_price + 1
        white_large_price = black_large_price + 1

        if coffee_type == "black":
            if coffee_size == "small":
                final_price = black_small_price
            elif coffee_size == "medium":
                final_price = black_medium_price
            elif coffee_size == "large":
                final_price = black_large_price
        else:
            if coffee_size == "small":
                final_price = white_small_price
            elif coffee_size == "medium":
                final_price = white_medium_price
            elif coffee_size == "large":
                final_price = white_large_price
        print("Your total cost is $" + str(final_price))
    else:
        print("Invalid size. Please choose small, medium, or large.")

else:
    print("Invalid type. Please choose black coffee or white coffee.")


# 5. Accumulation
low_value = int(input("Enter the low value: "))
high_value = int(input("Enter the high value: "))
while high_value <= low_value:
    print("Invalid input. Please enter a valid value, "
          "the high value must be greater than the low value.")
    high_value = int(input("Enter the high value again: "))
total_value = 0
for i in range(low_value, high_value + 1):
    print(i, end='')
    total_value += i
print(f"\nTotal: {total_value}")