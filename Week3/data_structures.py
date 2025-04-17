# myVarArray = ["apple", "banana", "cherry"]
#
# print(myVarArray)
#
# myVarArray.append("blueberry")
# # myVarArray[len(myVarArray):] = ["blueberry"]
#
# print("Append: " + str(myVarArray))
#
# myVarArray.insert(1, "randomItem")
#
# print("Insert: " + str(myVarArray))
#
# newList = ["car", "speaker", "laptop"]
#
# myVarArray.extend(newList)
#
# print("Extend: " + str(myVarArray))

#   0 1 2  3 4 5
a = [7,2,3,7,8]
b = [4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

a[3:3] = b
a[len(a):] = [9] # hasta este punto el resultado es [7, 2, 3, 4, 5, 6, 7, 8, 9]

# Delete an item
# a = a[:len(a) - 1]
# a.remove(7) # this removes an item looking for the first occurrence of the VALUE

# a.pop(1) # this removes an item at a specific INDEX

# a.remove()

def erase_second_ocurrence(arr, whatAreWeLookingFor, elementAtPosition):
    count = 0
    for index, element in enumerate(arr):
        if(element == whatAreWeLookingFor):
            count += 1
            if(count == elementAtPosition):
                arr.pop(index)
                break

# if(7 != "7"):
#     print("we are not the same")
# else:
#     print("we are :(")
# erase_second_ocurrence(a, "7", "2")
#
# print(a)


# Algo:

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
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
# Output: [0, 1]

numbers = [2, 7, 11, 15]
tar = 9


# n ^ 2
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []  # No solution found

# n
# def twoSum(nums, target):
#     numMap = {}
#     n = len(nums)
#
#     for i in range(n):
#         complement = target - nums[i]
#         if complement in numMap:
#             return [numMap[complement], i]
#         numMap[nums[i]] = i
#
#     return []  # No solution found
#
#
# twoSum(numbers, tar)
#
#
# erase_second_ocurrence(a, 7, 10)
#
# print(a)

# 📝 Problem Statement:
# You are building a simplified version of a recommendation system like those used in TikTok or Instagram.
#
# Given:
#
# A list of user likes with content IDs.
#
# A dictionary mapping each content ID to its tags.
#
# Your task is to generate a feed of recommended content IDs based on the most frequently interacted tags.
#
# The goal is to recommend content the user hasn't interacted with yet, but matches the tags they seem to like.

# likes = [
#     101, 103, 104
# ]

#  liked_tags = [travel, beach, mountains]
#
# content_tags = {
#     "101": ["travel", "beach"],
#     "102": ["food", "cooking"],
#     "103": ["travel", "mountains"],
#     "104": ["travel", "city"],
#     "105": ["cooking", "easy"],
#     "106": ["beach", "sun"],
#     "107": ["mountains", "hiking"],
#     "108": ["fashion"]
# }
#
# k = 3

# output = [106, 107, 105]

def recommend_feed(interactions: set[int], content_tags: dict[int, set[str]]) -> set[int]:
    liked_set = set()

    # Save important tags which user have interacted
    for element in interactions:
        if element in content_tags:
            liked_set.update(content_tags.get(element))

    future_recommendation = set()

    for key, value in content_tags.items():
        if key in interactions:
            continue  # Skip already seen content

        for element in value:
            if element in liked_set:
                future_recommendation.append(key)  # Negative for descending sort
                break

    return future_recommendation




likes = {
    101, 102, 103, 104
}

content_tags = {
    101: {"travel", "adventure"},
    102: {"food", "recipes", "easymeals"},
    103: {"fitness", "gym"},
    104: {"technology", "gadgets"},
    105: {"mentalhealth", "wellness"},
    106: {"travel", "photography"},
    107: {"gaming", "esports"},
    108: {"fashion", "style"},
    109: {"fitness", "yoga"},
    110: {"books", "reading"},
    111: {"finance", "investing"},
    112: {"cooking", "vegan"},
    113: {"parenting", "lifestyle"},
    114: {"pets", "dogs"},
    115: {"fashion", "trends"},
    116: {"technology", "programming"},
    117: {"fitness", "nutrition"},
    118: {"gaming", "strategy"},
    119: {"art", "design"},
    120: {"travel", "culture"}
}


print(recommend_feed(likes, content_tags))

likes = recommend_feed(likes, content_tags)

print(recommend_feed(likes, content_tags))






















