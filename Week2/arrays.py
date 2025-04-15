myList = ["apples", "banana", "cherry", "ham", "cheese", "orange", "coffee"]

# print(myList)
# subList = myList[3:]
# print(myList[:3])
#
# 1. Find the Maximum Number
# Problem:
# Given an array of integers, return the maximum value.
#
# Example:
# Input: [1, 5, 3, 9, 2]
# Output: 9

integerArray = [100, 5, 3, 9, 2, 1, 7, 56, 3, 4, 32]
invalidArray = []
validArray = [0]

# Assumption: No negative numbers
# def max_value(numArr):
#     current_max = -1
#     for x in numArr:
#         if x > current_max:
#             current_max = x
#
#     return current_max
#
# def min_value(numArr):
#     current_min = numArr[0]
#     for x in numArr[1:]:
#         if x < current_min:
#             current_min = x
#
#     return current_min
#
#
# print(max(integerArray))
#
# print(min(integerArray))

# C - Create
# R - Read
# U - Update
# D - Delete

def countdown(intialCount):
    print("Ready for take-off")
    while intialCount >= 0:
        print(intialCount)

        if(intialCount == 0):
            print("good bye!")

        intialCount = intialCount - 1


countdown(5)