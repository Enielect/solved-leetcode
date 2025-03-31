# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         valid = ''
#         for ele in s:
#             if ord(ele) in range(ord('a'),ord('z')+1) or ord(ele) in range(ord('A'),ord('Z')+1):
#                 print(ele)
#                 valid += ele
#         return valid[::-1].lower() == valid.lower()
    
# soln = Solution()

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         valid = ''
#         for ele in s:
#             if ele.isalnum():
#                 valid += ele
#         return valid[::-1].lower() == valid.lower()
    
# soln = Solution()

# I just a saw a good solution on leetcode

class Solution:
    def isPalindrome(self, s: str) -> bool:
          res = [x.lower() for x in s if x.isalnum()]
          return all(res[i] == res[~i] for i in range(len(s)//2))
    
# Operator ~ is the bitwise NOT operator. It performs logical negation on a given number by flipping all of its bits: ~x == -x-1 , ~0 == -1, ~1 == -2 and etc.

soln = Solution()

# I have to try one using two pointers later

## I just realised that you can check for alphanumeric digits in python by using the method: isalnum() on the character
print(soln.isPalindrome("A man, a plan, a canal: Panama"))