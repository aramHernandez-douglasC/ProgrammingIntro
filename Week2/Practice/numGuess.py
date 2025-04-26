# Number Guessing Game
#    - Create a secret number (e.g., 7)
#    - Keep asking the user to guess until they get it right
#    - Give hints: “Too high” or “Too low”
#    - Show number of attempts when they win
import random

def guess_a_number():
    computer_guess = random.randrange(0, 5)
    # print(f"DEBUG: Curr value of computer: {computer_guess}")
    try:
        print("Guess-a-number game")
        user_input = input("Pick a number from 0 to 5 and let's see if you know what I'm thinking: ")

        while user_input != computer_guess:
            if user_input > computer_guess:
                print("Too high!")
            elif user_input < computer_guess:
                print("Too low!")
            user_input = input("Pick a number from 0 to 5 and let's see if you know what I'm thinking: ")
    except ValueError as e:
        print(f"Something went wrong Reason: {e}")
        guess_a_number()
    except Exception as ex:
        print(f"I don't know {ex}")
        exit()

    print(f"Nice your guess was: {user_input}, and cpu was: {computer_guess}")


guess_a_number()