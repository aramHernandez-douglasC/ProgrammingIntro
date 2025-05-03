# Conditionals:
# If something is true then do something

# Conditional operators
# >
# <
# ==
# >=
# <=

# silvanaAge = 18
# silvanaTshirt = "red"
#
# johnAge = 19
# johnTshirt = "red"
#
# ferAge = 21
# ferTshirt = "blue"
#
# aramAge = 16
# aramTshirt = "black"
#
#
# def is_eligible(personAge, colorTshirt):
#     if ((personAge >= 19) and (colorTshirt == "red")):
#         print("Great you can enter")
#     elif ((personAge == 18)) and (colorTshirt == "red"):
#         print("Gtfo Silvana")
#     else:
#         print("Sorry you cannot pass iugh")
#
# is_eligible(ferAge, ferTshirt)

# % = modulo
# def is_even_or_odd(num1):
#     if (num1 % 2 == 0):
#         print(str(num1) + " is even")
#     else:
#         print(str(num1) + " is odd")
#
# is_even_or_odd()
#
#
# def can_vote(age):
#     # if person age is >= 18
#     if (age >= 18):
#         print("eligible to vote")
#     else:
#         print("not eligible to vote")
#
# Checks is a number is bigger, less or equal
# def compare_numbers(num1, num2):
#     if(num1 > num2):
#         print(str(num1) + " is bigger than " + str(num2))
#     elif(num2 > num1):
#         print(str(num2) + " is bigger than " + str(num1))
#     elif(num2 == num1):
#         print(str(num2) + " is equal to " + str(num1))
#
# compare_numbers(5, 10)
#
#
#
# Return "Fizz" if divisible by 3,
# "Buzz" if divisible by 5,
# "FizzBuzz" if divisible by both,
# else the number as a string.
# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
#
#
# fizzbuzz(3) # fizz
# fizzbuzz(10)  # buzz
# fizzbuzz(15) # FizzBuzz
# fizzbuzz(7) # 7

# Description:
# Return the price after discount:
#
#  - Under 18 → 20% off
#
#  - 18–60 → No discount
#
#  - Over 60 → 30% off
# def apply_discount(age, price):
#     if(age < 18):
#         return price - (price * 0.20)
#     elif(age > 60):
#         return price - (price * 0.30)
#     else:
#         return price
#
# tshirtPrice = 60.0
# pantsPrice = 120.0
# hatPrice = 10.0
# skirtPrice = 24.99
#
# print(apply_discount(75, skirtPrice))


# SWITCH or match case Python 3.10+

# def simple_calculator(num1, num2, operator):
#     match operator:
#         # if(op == "+")
#         case "+":
#             return num1 + num2
#         case "x":
#             return num1 * num2
#         case "-":
#             return num1 - num2
#         case "/":
#             return num1 / num2
#         # Default
#         case _:
#             return "Not supported"
#
# #
# print(simple_calculator(100, 50, "@"))



