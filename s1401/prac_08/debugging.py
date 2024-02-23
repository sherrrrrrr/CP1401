"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(1, len(names)):
# print(f"{i}. {names[i]}")
# last_number = len(names)
# print(f"The last name (number {last_number}) is {names[last_number]}")

# Problem(s) for program 1:
#  The loop in the range of 1 to len(names) causes the code to skip printing the first name in the list.

# Fixed code for program 1:
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")
last_number = len(names) - 1
print(f"The last name (number {last_number+1}) is {names[last_number]}")


# Debug program 2 - title-casing country names
# countries = ("australia", "new zeaLAND", "India")
# for i in range(len(countries)):
# countries[i] = countries[i].title()
# print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# Tuple objects are immutable, so the code cannot modify the country names in place by assigning them the title-cased versions.

# Fixed code for program 2:
countries = ("australia", "new zeaLAND", "India")
titlecased_countries = tuple(country.title() for country in countries)
print(titlecased_countries)