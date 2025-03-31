class Stack:
    def __init__(self):
        self.arr = []
    def peek(self):
        if not self.arr:
            return []
        return self.arr[len(self.arr)-1]
    def pop(self):
        return self.arr.pop()
    def push(self,i):
        self.arr.append(i)
    def is_empty(self):
        return self.arr == []

# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         #peek, pop, push, 
#         final = ''
#         stack = Stack()
#         count = 1
#         for ch in s:
#             check = []
#             if stack.is_empty():
#                 stack.push(ch)
#                 continue
#             count = 1
#             while ch == stack.peek() and count < k:
#                 check.append(stack.pop())
#                 count +=1
#             if  count != k:
#                 for i in check:
#                     stack.push(i)
#                 stack.push(ch)
#         while stack.peek():
#             final += stack.pop()
#         return final[::-1]
        
#Lol, I had a TLE on the 17/21 test case, omo

# massively improved solution
# we used an array that stores a tuple as our stack
# The logic is better

class Solution:
    def removeDuplicates(self, s:str, k:int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1] = (ch, stack[-1][1] + 1)   
            else:
                stack.append((ch,1))
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(ch * count for ch,count in stack)
    
# what i learned from here is that as for as you are looking for adjacent elements you can use a stack
# to ensure that you only use an O(n) time complexity, because the consequent popping, and pushing
# will always balance out.

print(Solution().removeDuplicates("abcd",2)) #expected: "abcd"
print(Solution().removeDuplicates("deeedbbcccbdaa",3)) #expected: "aa"
print(Solution().removeDuplicates("pbbcggttciiippooaais",2)) #expeceted: "ps"
