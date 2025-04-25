# def two_sum(nums: list[int], target: int):
#     n = len(nums)
#     for OuterPointer in range(n -1):
#         for InnerPointer in range(OuterPointer +1,n):
#             if nums[InnerPointer] + nums[OuterPointer] == target:
#                 return [OuterPointer,InnerPointer] 
#     return []

import random

def guess_a_number():
    computer_guess = random.randint(1,5)

    print("Guess a number game!")
    user_input = int(input("Pick a number from 0-5 and let's see if you know what I am thinking: "))  

    while user_input != computer_guess:
        if user_input > computer_guess:
            print ("Too High!")
        elif user_input < computer_guess:
            print ("Too Low!")
        user_input = int(input("Try again:"))
    print("Correct!")

        
          
guess_a_number()


        





# numbers = [3, 2, 4]
# target = 6

# print(two_sum(numbers,target))


# Algo:

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
# to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example
# 1:
#
# Input: nums = [2, 7, 11, 15], target = 9

# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].

# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]