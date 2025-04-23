import random
# How to read input from console
# Reading input from user is an essential skill required to evaluate our code using a user's scenario

def read_from_user():
    print("Give me 2 numbers to sum.")

    # Extract the user input from the console and store the value in a variable
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")

    # Since all the input variables will return a string, we have to convert the values to integers to make the addition
    result = int(num1) + int(num2)

    print(f"The result from adding {num1} and {num2} is {result}")


# read_from_user() # <- run this code line to see what happens in your console :)


# We can also keep reading the user input until certain condition is met using a while loop
def guess_color():
    # 1. We store a list of possible options to choose from
    colors = ['red', 'blue', 'orange', 'magenta', 'white', 'black', 'yellow', 'green', 'cyan']

    # 2. We make the computer choose one of the options randomly using the random library.
    cpu_selection = random.choice(colors)

    print("Which color am I thinking of? \n"
          "Options: red, blue, orange, magenta, white, black, yellow, green or cyan")

    # 3. We store the prompt we will be using at the start and each time the user incorrectly chooses a color
    #    The reason why we store it in a variable is to avoid duplicating the string contained within the prompt itself
    prompt = "Give me your best guess here: "

    # 4. We ask the user to write their option in the console and store it in a variable
    user_color = input(prompt)
    tries = 1

    # 5. We initialize the loop and add a condition stating that "As long as the user's choice is not the same as the
    #    computer's, keep running the instructions within"
    while user_color != cpu_selection:
        tries += 1  # We add 1 to our counter each time the user selection is incorrect
        print("Bad guess, try again")
        user_color = input(prompt)  # we retrieve the user input again until he guesses the computer's choice

    # 6. Once the user has found the correct choice the loop will end, and we will print what the computer's choice
    #    was, what is the user input and the amount of attempts it took.
    print(f"Nice you chose the correct one. Cpu choice: {cpu_selection}, Your choice: {user_color}. Tries = {tries}")

guess_color() # <- run this code line to see what happens in your console :)

