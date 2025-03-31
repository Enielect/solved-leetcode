# I had some edge cases which I didn't consider, for instance when there is only a closing bracker in the string
# or when there are only clsoing braces in the string. 

# Then the other edge case was this example string: [}], if we don't push an opening for the '{}'
# then we dont account for the invalidity of this string, so i had to fix that by adding a count

# my approach shown below

# opcl = dict(('()', '[]', '{}')) (I'll come to this a little later)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         count = 0
#         for ch in s:
#             if ch in '([{':
#                 stack.append(ch)
#                 count +=1
#                 continue
#             if not stack:
#                 return False
#             if '([{'.index(stack[-1]) == ')]}'.index(ch):
#                 # I did some useless anding for each case for the above before.
#                 stack.pop()
#                 count -=1
#             else:
#                 count +=1
#         return stack == [] and count == 0
    
#python solution from the comments no leetcode

class Solution(object):
    def isValid(self, s):
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}')) # This create a dictionary: {'(': ')', '[': ']', '{': '}'}
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0 # I think this is an edge case for when only on element(an opening braces) exists in the string.
        # if not we might just have returned True (return True)
    
    
print(Solution().isValid("([[]])"))