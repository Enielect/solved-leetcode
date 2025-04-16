from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         #brute force solution:
#         # I kind of knew that this wold give TLE as I was nesting 3 times.
#         res = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     sorted_triplet = sorted([nums[i],nums[j],nums[k]])
#                     if nums[i] + nums[j] + nums[k] == 0 and sorted_triplet not in res:
#                         res.append(sorted_triplet)
#         return res
    
    # A revised solution
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, left, right = [], 0, len(nums) - 1
        nums.sort()
        print(nums)
        for i in range(1,len(nums) -1):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                target = -1 * (nums[left] + nums[right])
                if target == nums[i]:
                    res.append([nums[left],nums[right],nums[i]])
                    break
                if target < nums[i] or i == right:
                    right -=1
                elif target > nums[i] or i == left:
                    left +=1
        return res
    
print(Solution().threeSum([-1,0,1,2,-1,-1,-4,-1]))
# print(Solution().threeSum([0,1,1]))
# print(Solution().threeSum([0,0,0,0]))