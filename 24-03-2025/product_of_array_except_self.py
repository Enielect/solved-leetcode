from typing import List
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my idea is to iterate throught array once but slice the array as we move
        res = []
        for i,num in enumerate(nums):
            left = nums[:i]
            right = nums[i+1:]
            if left and right:
                left_reduced = reduce(lambda a,b: a*b, left)
                right_reduced = reduce(lambda a,b: a*b, right)
                res.append(left_reduced*right_reduced)
            elif left:
                res.append(reduce(lambda a,b: a*b, left))
            else:
                res.append(reduce(lambda a,b: a*b, right))
        return res
# print(Solution().productExceptSelf([1,2,3,4]))

# The one suggessted by deepseek: using prefixes and suffixes
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # my idea is to iterate throught array once but slice the array as we move
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] *=prefix
            prefix *=nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res