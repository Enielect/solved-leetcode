from typing import List
#my solution to the twosum problem usng two-pointer
def two_sum(list: List[int], target: int) -> bool:
    #note that the input is sorted
    left = 0, right = len(list) - 1
    
    while left < right:
        sum = list[left] + list[right]
        if sum == target:
            return True
        elif sum > target:
            right -=1
        else:
            left +=1
    return False
            
            
print(two_sum([10, 20, 35, 50], 70))
print(two_sum([-3, -1, 0, 1, 2], -2))