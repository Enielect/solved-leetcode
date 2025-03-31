from typing import List


def containsNearbyDuplicate( nums: List[int], k: int) -> bool:
    #set up a dictionary to keep track of previously seen index of a particular number
    track = {}
    ##we loop through each element of the list
    for i,j in enumerate(nums):
        if j in track:
            #if the element has already been seen before
            if abs(track.get(j) - i) > k:
                #we check if the stored index is greater than the present one
                #if so we update the dictionary with the current one
                 track[j] = i
            else:
                #if the stored index is less than or equal to the present one, we just return True
                return True
        else:
            #If the element did not previously exist in the dictionary, we add it, with its current index
            track[j] = i
    return False

print(containsNearbyDuplicate([1,2,2,1], 1)) # true
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) #false
print(containsNearbyDuplicate([1,2,3,1],3)) # true
print(containsNearbyDuplicate([1,0,1,1], 1)) # true