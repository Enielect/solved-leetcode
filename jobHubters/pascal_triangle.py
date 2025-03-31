from typing import List


def generate(numRows: int) -> List[List[int]]:
    base_case = [[1],[1,1]]
    if numRows == 1:
        return [[1]]
    elif numRows > 2:
        for i in range(2,numRows):
            base = [1,1]
            for j in range(1,i):
                previous = base_case[i-1]
                base.insert(j,previous[j] + previous[j-1])
            base_case.append(base)
        return base_case
    else:
        return [[1],[1,1]]
    
print(generate(5))