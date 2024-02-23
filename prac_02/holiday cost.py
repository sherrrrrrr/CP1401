# 3. Holiday Cost
daily_food_cost = float(input("Daily Food Cost: $"))
daily_activities_cost = float(input("Daily Activities Cost: $"))
number_of_days = float(input("Number of days = "))
trip_cost = (daily_food_cost + daily_activities_cost + 75) * number_of_days
print("The trip will cost $", trip_cost, sep="")