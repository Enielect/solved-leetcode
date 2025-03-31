from typing import List

# def summaryRanges(nums: List[int]) -> List[str]:
#     #in the end it is the idea to solve the problem, and not exactly following some particular syntax
#     #intialize two pointers that track the range.
#     if not nums:
#         return []
#     result = []
#     left = 0
#     while left < len(nums):
#         right = left
#         while right + 1 < len(nums) and nums[right + 1] - nums[right] == 1:
         #while len(nums) - 1 >= right and nums[right + 1] - nums[right] == 1:(this will give you the problem of list out of range because
         # right firstly is not bounded by the condition of the while loop, and so the revision here is better)

#             right +=1
#         if right != left:
#             result.append(f'{nums[left]}->{nums[right]}')
#         else:
#             result.append(f'{nums[left]}')
#         left = right+1
#     return result

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))