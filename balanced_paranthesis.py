# (()((())()))

#implement a stack

#stack operations: peek, size, pop, push, is_mpty, 

class Stack:
    def __init__(self):
        self.list = []
        
    def peek(self):
        return self.list[len(self.list) - 1]
    def size(self):
        return len(self.list)
    def pop(self):
        return self.list.pop()
    def push(self, ele):
        self.list.append(ele)
    def is_empty(self):
        return len(self.list) == 0

def balenced_paranthesis(sample):
    