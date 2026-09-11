# 1. Two Sum 
# def twoSum(nums, target):
#     map = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in map:
#             return [map[diff], i]
#         map[num] = i

def twoSum(nums, target):
  map = {}
  for i, num in enumerate(nums):
    dif = target - num
    if dif in map:
      return [map[dif], i]
    map[num] = i