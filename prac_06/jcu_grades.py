"""3. JCU grades"""
import random
def main():
    while True:
        score = float(input("Score: "))
        if score < 0:
            break
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")

    num_random_scores = int(input("How many random scores: "))
    for _ in range(num_random_scores):
        random_score = random.uniform(0, 100)
        grade = determine_grade(random_score)
        print(f"{random_score:.0f} = {grade}")
def determine_grade(score):
    """determines the JCU grade based on the score."""
    if score < 50:
        return 'F'
    elif score < 65:
        return 'P'
    elif score < 75:
        return 'C'
    elif score < 85:
        return 'D'
    else:
        return 'HD'

def test_determine_grade():
    """tests the determine_grade function, check the grade for that score."""
    assert determine_grade(49) == 'F'
    assert determine_grade(50) == 'P'
    assert determine_grade(64) == 'P'
    assert determine_grade(65) == 'C'
    assert determine_grade(74) == 'C'
    assert determine_grade(75) == 'D'
    assert determine_grade(84) == 'D'
    assert determine_grade(85) == 'HD'
    assert determine_grade(100) == 'HD'
    print("All tests passed.")
# test function
# test_determine_grade()

# run that program
main()
