from typing import List


def countDays(days: int, meetings: List[List[int]]) -> int:
    res = set()
    for num in meetings:
        left = num[0]
        right = num[1]
        res = res.union(range(left, right + 1))
    return days - len(res)
        

print(countDays(10,[[5,7],[1,3],[9,10]]))
