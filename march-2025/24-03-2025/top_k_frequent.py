from collections import defaultdict
from typing import List

#my initial approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        original_dict = defaultdict(list)
        for num in nums:
            if num in original_dict:
                original_dict[num] +=1
            else:
                original_dict[num] = 1
        sorted_dict = dict(sorted(original_dict.items(), key = lambda item: item[1], reverse=True)) 
        return list(sorted_dict.keys())[0:k]
    
    
soln = Solution()
print(soln.topKFrequent([1],1), 'first_soln')
#what i lerned from deepseek(lol, it is the the propietary owner)

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Learning the bucket sort method
    freq = defaultdict(int)
    for num in nums:
        freq[num] +=1
    bucket = [[] for _ in range(len(nums) + 1)] # This is because, in the case that there is only one element in the list, count, which would be 1 would always exist as an index in the list
    for key,count in freq.items():
        bucket[count].append(key)
    res = []
    for ele in range(len(bucket)-1, -1, -1):
        res.extend(bucket[ele])
        if len(res) >= k:
            break
    return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1],1))


#below is the min-heap solution that deepseek suggested

# resource: https://docs.python.org/3/library/heapq.html

# import heapq
# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = defaultdict(int)
#         for num in nums:
#             freq[num] += 1
        
#         # Use a min-heap of size k
#         heap = []
#         for num, count in freq.items():
#             heapq.heappush(heap, (count, num))
#             if len(heap) > k:
#                 heapq.heappop(heap)
        
#         return [num for (count, num) in heap]