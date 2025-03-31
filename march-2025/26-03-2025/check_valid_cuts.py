from typing import List

# This solution is wrong, i have to retry now

# def checkValidCuts(n: int, rectangles: List[List[int]]) -> bool:
#     y_sort = sorted(rectangles, key=lambda i:i[1])
#     x_sort = sorted(rectangles, key=lambda i: i[0])
#     y_count = 0
#     x_count = 0
#     print(x_sort,'x')
#     print(y_sort, 'y')
#     for i,rect in enumerate(y_sort):
#         if y_count and y_sort[i-1][1] != rect[1]:
#             y_count +=1
#             if y_count == 3:
#                 return True
#         if not y_count:
#             y_count +=1
#     for j,rect in enumerate(x_sort):
#         if x_count and x_sort[j-1][0] != rect[1]:
#             x_count +=1
#             if x_count == 3:
#                 return True
#         if not x_count:
#             x_count +=1
#     return False 

def checkValidCuts(n: int, rectangles: List[List[int]]) -> bool:
        x_cut = 1
        y_cut = 1
        y_init = f'{rectangles[0][1]}'
        x_init = f'{rectangles[0][2]}'
        for i in range(1,len(rectangles)):
            y_ele = f'{rectangles[i][1]}'
            x_ele = f'{rectangles[i][0]}'
            if y_ele not in y_init:
                y_init +=y_ele
                y_cut +=1
            if x_ele not in x_init:
                x_init +=x_ele
                x_cut +=1
        return x_cut > 2 or y_cut > 2
    

print(checkValidCuts(5,[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))
print(checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))
