def divideArray(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    final = []
    for index, ele in enumerate(nums):
        if index % 2 == 0:
            if index + 1 == len(nums):
                break
            if nums[index] == nums[index + 1]:
                final.append(True)
            else:
                final.append(False)
    return all(final)
    
print(divideArray([15,13,5,20,18,2,20,8,20,17,10,19]))