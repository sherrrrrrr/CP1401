"""
CP1401 2023-SP53 Assignment 1
Program 1 – Police School Results
Student Name: <Jiaxin Li>
Date started: <2023.12.06>

Pseudocode:
display "Welcome Trainee Police. How did you do?"
# Input
get practical_score, exam_score
# Processing
total_score = practical_score + exam_score
# Output
if total_score < 50:
    display "You failed the police exam. Please try again next year."
else:
    if exam_score <= practical_score:
        display "You will become an undercover cop."
    else:
        display "You will become a motorcycle cop."

    if total_score >= 95:
        display "Congratulations on making the honour roll!"
"""

print("Welcome Trainee Police. How did you do?")
# Input
practical_score = int(input("Practical score (0-50): "))
exam_score = int(input("     Exam score (0-50): "))
# Processing
total_score = practical_score + exam_score

print(f"Your total score is {total_score} out of 100.")
# Output
if total_score < 50:
    print("You failed the police exam. Please try again next year.")
else:
    if exam_score <= practical_score:
        print("You will become an undercover cop.")
    else:
        print("You will become a motorcycle cop.")

    if total_score >= 95:
        print("Congratulations on making the honour roll!")