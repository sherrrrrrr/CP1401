subject_score_1 = float(input("Enter your subject score 1: "))
subject_score_2 = float(input("Enter your subject score 2: "))
subject_score_3 = float(input("Enter your subject score 3: "))
total_score = subject_score_1 + subject_score_2 + subject_score_3
average_score = total_score / 3
print("The total score is ", total_score, sep="")
print("The average score is ", average_score, sep="")

TOTAL_SUBJECT = 3
TOTAL_SCORE = 9
average_score = TOTAL_SCORE/TOTAL_SUBJECT
for i in range(TOTAL_SCORE):
    subject_score = float(input("Enter ", {i+1}, average_score))
    total_score += subject_score * 3

    print(("Total score is ", total_score, "The average score is ", average_score))

# 2. Determine average score
subject_score_1 = (input("Enter your subject 1 score: "))
subject_score_2 = (input("Enter your subject 2 score: "))
subject_score_3 = (input("Enter your subject 3 score: "))
total_score = subject_score_1 + subject_score_2 + subject_score_3
average_score = (subject_score_1 + subject_score_2 + subject_score_3)/3
if average_score <= 10:
    print("Fail")
elif 10 < average_score <= 20:
    print("Pass")
elif 20 < average_score <= 30:
    print("Credit")
elif average_score > 30:
    print("Excellent")


score = {18, 11, 24, 32}
fail_count = 0
pass_count = 0
credit_count = 0
excellent_count = 0
if score <= 10:
    message = "Fail"
elif score <= 20:
    message = "Pass"
elif score <= 30:
    message = "Credit"
else:
    message = "Excellent"

average_score = float(input("Enter the average score: "))
print("Enter the average score: ")
if average_score >= 0 or average_score <= 10:
    print("Fail")
elif 10 < average_score <= 20:
    print("Pass")
elif 20 < average_score <= 30:
    print("Credit")
else:
    print("Excellent")


# 3. Validate user input. Score 0-100
while score <=0 or score > 100:
    print("Invalid")