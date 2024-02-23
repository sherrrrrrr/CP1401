record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]

last_name = record[1]
born_date = record[2]

# Print extracted data
print("Last name:", last_name)
print("Born:", born_date)
print(record[0], "was born in", born_date[2], "and was a great", record[3], "player.")