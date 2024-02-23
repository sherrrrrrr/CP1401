"""
Pseudocode:
start program

function main()
    sum_scores = 0
    scores = []

    for i in range(4)
        score = get_score(i + 1)
        grade = convert_to_grade(score)
        print("Score " + str(i + 1) + " was " + "{:.1f}".format(score) + " which is " + grade)
        sum_scores = sum_scores + score
        scores.append(score)

    average_score = sum_scores / length(scores)
    display("The average score was {:.3f}".format(average_score))

    if scores[last_index(scores)] > average_score
        trend = "positive"
    else:
        trend = "not positive"
    display("The trend is " + trend)

function get_score(scores)
    while true
        score = input("Score " + str(scores) + ": ")
        score = float(score)
        if score >= 0 and score <= 100
            return score
        else:
            display("Invalid score. Please enter a score between 0 and 100.")

function convert_to_grade(score)
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "N"

if __name__ == '__main__'
    main()

end program
"""
def main():
    sum_scores = 0
    scores = []

    for i in range(4):
        score = get_score(i + 1)
        grade = convert_to_grade(score)
        print("Score " + str(i + 1) + " was " + "{:.1f}".format(score) + " which is " + grade)
        sum_scores += score
        scores.append(score)

    average_score = sum_scores / len(scores)
    print("The average score was {:.3f}".format(average_score))

    if scores[-1] > average_score:
        trend = "positive"
    else:
        trend = "not positive"
    print(f"The trend is {trend}")
def get_score(scores):
    while True:
        score = input("Score " + str(scores) + ": ")
        score = float(score)
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    else:
        print("Invalid input. Please enter a valid score.")

def convert_to_grade(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "N"

if __name__ == '__main__':
    main()
