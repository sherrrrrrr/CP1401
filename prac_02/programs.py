# 1. Discount Price
original_price = float(input("Original price: $"))
discount_rate = float(input("Discount Rate (e.g. 0.2): "))
discount = original_price * discount_rate
new_price = original_price - discount
print("The new price is $", new_price, sep="")

# 2. Kilometres to Miles
kilometre = float(input("kilometre : "))
conversion_rate = 0.621371
mile = kilometre * conversion_rate
print("The Miles is ", mile, sep="")

# 3. Holiday Cost
daily_food_cost = float(input("Daily Food Cost: $"))
daily_activities_cost = float(input("Daily Activities Cost: $"))
number_of_days = float(input("Number of days = "))
trip_cost = (daily_food_cost + daily_activities_cost + 75) * number_of_days
print("The trip will cost $", trip_cost, sep="")

# 4. Deep Sleep Calculation(Percentage)
Total_sleep_in_seconds = float(input("Total Sleep in seconds : "))
Deep_sleep_in_seconds = float(input("Deep Sleep in seconds : "))

Total_sleep_in_mintues = Total_sleep_in_seconds / 60
Deep_sleep_in_mintues = Deep_sleep_in_seconds / 60
Percentage = (Deep_sleep_in_mintues / Total_sleep_in_mintues ) * 100
print("The percentage is ", Percentage, sep="")



