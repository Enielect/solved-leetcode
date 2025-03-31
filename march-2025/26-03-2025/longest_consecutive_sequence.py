from typing import List

# def longestConsecutive(nums: List[int]) -> int:
#     check = sorted(list(set(nums)))
#     print(check)
#     res = [1] * len(nums)
#     index = 1
#     res_index = 0
#     while index < len(check):
#         if check[index] == check[index-1] + 1:
#             res[res_index] +=1
#         else:
#             res_index +=1
#         index +=1
#     return max(res)

## There was a better solution with set
def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    res_set = set()
    current_length = 1
    max_length = 1
    for num in nums_set:
        current = num
        if num in res_set:
            continue
        while current + 1 in nums_set:
            res_set.add(current)
            current_length +=1
            current +=1
        max_length = max(max_length, current_length)
        current_length = 1
    return max_length   

#optimized by copilot

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    nums_set = set(nums)
    max_length = 1
    for num in nums_set:
        if num -1 in nums_set:
            continue
        current = num
        current_length = 1
        while current + 1 in nums_set:
            current_length +=1
            current +=1
        max_length = max(max_length, current_length)
    return max_length  


print(longestConsecutive([1,0,1,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([100,4,200,1,3,2]))