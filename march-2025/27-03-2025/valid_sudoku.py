from collections import defaultdict
from typing import List

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #managing the subgrid
#         subgrid_dict = defaultdict(list)
#         vertical_dict = defaultdict(list)
#         for i in range(len(board)):
#             for j in range(len(board)):
#                 index_sub = f"{j//3}-{i//3}"
#                 if board[i][j] == '.':
#                     continue
#                 if int(board[i][j]) > 9:
#                     return False
#                 subgrid_dict[index_sub].append(board[i][j])
#                 vertical_dict[j].append(board[i][j])
#                 subgrid = subgrid_dict[index_sub]
#                 if len(set(subgrid)) != len(subgrid):
#                     return False
#                 if len(set(vertical_dict[j])) != len(vertical_dict[j]):
#                     return False
#             filtered = [x for x in board[i] if x != '.']
#             if len(set(filtered)) != len(filtered):
#                 return False
#         return True
# soln = Solution()


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #managing the subgrid
        subgrid_set = defaultdict(set)
        row = defaultdict(set)
        vertical_set = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                index_sub = f"{j//3}-{i//3}"
                if num == '.':
                    continue
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)
                if num in subgrid_set[index_sub]:
                    return False
                else: 
                    subgrid_set[index_sub].add(num)
                if num in vertical_set[j]:
                    return False
                else:
                    vertical_set[j].add(num)
        return True
soln = Solution()

#Fucking crazy short solution from the solutions section from leetcode
def betterSolution(board: list[List[str]]) -> bool:
    res = []
    for i in range(9):
        for j in range(9):
            index = board[i][j]
            if index == '.':
                continue
            res += [(i,index),(index,j),(i//3,j//3,index)]
    return len(set(res)) == len(res)

#I saw that an optimized way of doing this is to use set

print(betterSolution([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(betterSolution([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(betterSolution([["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))