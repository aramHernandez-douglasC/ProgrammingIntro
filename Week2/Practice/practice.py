import random

# def print_prime_numbers(n : int):
#     prime_nums = {}
#     for num in range(2, n):
#         for curr in range(2, num):
#             if()
#
#     pass

# Option 1
# def rock_paper_scissors(user_input: str):
#     options = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(options)
#
#     if(user_input == "rock" and computer_choice == "paper") or (user_input == "paper" and computer_choice == "scissors") or (user_input == "scissors" and computer_choice == "rock"):
#         print("Computer wins.")
#
#     else:
#         print("User wins")
#
#     print(f"User chose {user_input} and CPU chose {computer_choice}")
#
def rock_paper_scissors(user_input: str):

    # Dictionary containing OPTION : WINNING OPPOSITE
    winning_dict = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    while (True):
        if user_input not in options:
            print("Invalid input.")
            continue

        print(f"User chose {user_input} and CPU chose {computer_choice}")
        if winning_dict.get(user_input) == computer_choice:
            print("Computer wins.")
            break
        elif user_input == computer_choice:
            print("Draw! try again")
            break
        else:
            print("User wins")
            break

def play():
    print("Let's play rock paper scissors. Good luck!")

    user_input = input("Make your choice: ")

    rock_paper_scissors(user_input)

play()

