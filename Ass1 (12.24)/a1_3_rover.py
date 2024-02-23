"""
CP1401 2023-SP53 Assignment 1
Program 1 – Mars Rover Tracker
Student Name: <Jiaxin Li>
Date started: <2023.12.06>

Pseudocode:
display "Rover Tracker"
# Input
get number_of_days, distances
# Processing
average_distance = total_distance / number_of_days
average_speed = total_distance / (number_of_days * 24)
average_distance_as_str = str(average_distance)
average_speed_as_str = str(average_speed)
average_distance_decimal_part = average_distance_as_str.split('.')[1]
# Output average distance
if average_distance_decimal_part.strip('0') == '':
    print(f"Your average distance was {average_distance:.1f} kilometres")   # Show average distance
else:
    print(f"Your average distance was {average_distance} kilometres")
# Output average speed
if average_speed_decimal_part.strip('0') == '':
    display "Your average distance was {average_speed:.1f} kilometres per hour"
else:
    display "Your average distance was {average_speed:.15f} kilometres per hour"
last_day_distance = distances[-1]
if last_day_distance > average_distance:
    display "On your final day, your distance was above average."
elif last_day_distance < average_distance:
    display "On your final day, your distance was below average."
else:
    display "On your final day, your distance was equal to average."
"""

print("Rover Tracker")
# Input number of days, distance
number_of_days = 0
while number_of_days < 1:
    number_of_days = int(input("Number of days: "))
    if number_of_days < 1:
        print("Invalid number of days")

total_distance = 0
distances = []

for day in range(1, number_of_days + 1):
    distance = -1

    while distance < 0 or distance > 100:
        distance = float(input("Day {} distance: ".format(day)))

        if distance < 0 or distance > 100:
            print("Invalid distance")

    distances.append(distance)
    total_distance += distance
# Processing
average_distance = total_distance / number_of_days
average_speed = total_distance / (number_of_days * 24)

average_distance_as_str = str(average_distance)
average_speed_as_str = str(average_speed)

average_distance_decimal_part = average_distance_as_str.split('.')[1]
average_speed_decimal_part = average_speed_as_str.split('.')[1]

print("Your total distance was   {:.1f} kilometres".format(total_distance))
# Output average distance
if average_distance_decimal_part.strip('0') == '':
    print(f"Your average distance was {average_distance:.1f} kilometres")   # Show average distance
else:
    print(f"Your average distance was {average_distance} kilometres")

# Output average speed
if average_speed_decimal_part.strip('0') == '':
    print(f"Your average distance was {average_speed:.1f} kilometres per hour")   # Show average speed
else:
    print(f"Your average distance was {average_speed:.15f} kilometres per hour")

last_day_distance = distances[-1]

if last_day_distance > average_distance:
    print("On your final day, your distance was above average.")
elif last_day_distance < average_distance:
    print("On your final day, your distance was below average.")
else:
    print("On your final day, your distance was equal to average.")
