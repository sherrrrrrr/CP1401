"""
Pseudocode:
start program

total = 0.0
count = 0

filename = input("Filename: ")
in_file = open(filename, 'r')

for line in in_file:
    score = float(line)
    total += score
    count += 1
    display "Score = {score:.1f}   Total so far = {total:.1f}"

in_file.close()
average = total / count
display "Average = {average:.1f}"
end program
"""
total = 0.0
count = 0

filename = input("Filename: ")
in_file = open(filename, 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:.1f}   Total so far = {total:.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")