"""CP1401 - Practical 10 - Debugging.
Explain the problems (not the solution, not the style issues):
1.  In the `get_valid_amount()` function, there is no check for
 invalid input when the user enters a non-numeric value.
2. In the `play()` function, there is an incorrect indentation
 level for the `print("Invalid choice")` statement. It should
 be aligned with the `if` statement.
3. In the `play()` function, we have to check if the random
 chance is within the specified range. The condition
 `risk_chance <= CONSERVATIVE_CHANCE` and `risk_chance <= AGGRESSIVE_CHANCE`
 should use the 'greater than' operator instead of 'less than or equal to'
 operator.
4.  There is not a return statement in the `play()`
 function for the case where the user makes an invalid choice.

Describe your debugging process:
1. I ran the code and found that if I enter an invalid amount
 or choice, the program displays "Invalid amount" or "Invalid choice",
 and then continues to prompt for a valid amount or choice without letting
 the user re-enter their input.
2. I noticed the indentation issue with the `print("Invalid choice")`
 statement and fixed it.
3. I identified the incorrect use of the 'less than or equal to' operator
 in the conditions `risk_chance <= CONSERVATIVE_CHANCE` and
 `risk_chance <= AGGRESSIVE_CHANCE`. I fixed the conditions by changing
  the operator to the 'greater than' operator.
4. I added a return statement in the `play()` function for the case where
 the user makes an invalid choice, so that the function returns a value.

Fix the code in-place below
"""
import random

VALID_CHOICES = 'AC'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 50
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 80


def main():
    money = 100
    print("Welcome to the futility of gambling!")
    print("You start with a balance of $100.")
    while money > 0:
        result = play(money)
        money = money + result
        print(f"Your new balance is ${money}")
    print("You lost :)")


def get_valid_amount(balance, amount):
    while amount < 0 or amount > balance:
        print("Invalid amount")
        amount = int(input("Enter amount to play: "))
    return amount


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount = int(input("Enter amount to play: "))
    amount_to_risk = get_valid_amount(balance, amount)
    choice = 'x'
    while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
                print("Invalid choice")
    risk_chance = random.randint(0, 101)
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = amount_to_risk * (CONSERVATIVE_REWARD / 100)
        print(f"Congratulations! You earned ${result:.2f}")
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = amount_to_risk * (AGGRESSIVE_REWARD / 100)
        print(f"Congratulations! You earned ${result:.2f}")
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
    return result


main()