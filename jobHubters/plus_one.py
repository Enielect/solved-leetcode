from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) -1
        while index >= 0:
            if digits[-1] != 9 and index == len(digits) -1:
                digits[-1]+=1
                break
            if digits[index] == 9:
                digits[index] = 0
            elif digits[index] != 9 and digits[index +1] ==0:
                digits[index] +=1
                break
            index -=1
        if all(x==0 for x in digits):
            digits.insert(0,1)
        return digits
    