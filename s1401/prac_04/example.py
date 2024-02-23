MINIMUM_MONTH = 1
MAXIMUM_MONTH = 10
month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

while month < MINIMUM_MONTH or month > MAXIMUM_MONTH:
    print("Invalid month")
    month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

for count in range(1, month + 1):
    print(count, end=" ")

print()



