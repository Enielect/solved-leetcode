
# Time complexity of O(n^2logn)
# class Solution:
#     def maxProfit(self, prices):
#         max_profit = 0
#         i = 0
#         while i in range(len(prices)):
#             sort_list = sorted(prices[i+1:])
#             if sort_list:
#                 diff = sort_list[-1] - prices[i]
#                 if prices[i] < sort_list[-1] and diff > max_profit:
#                     max_profit = diff
#             i += 1
#         return max_profit
            
# soln = Solution()
# print(soln.maxProfit([7,1,5,3,6,4]))
# print(soln.maxProfit([7,6,4,3,1]))


## A more time efficient solution (O(n^2)) //seems like it is still not good enough

# class Solution:
#     def maxProfit(self, prices):
#         max_profit = 0
#         i = 0
#         while i in range(len(prices)):
#             j = i+1
#             while j in range(len(prices)):
#                 diff = prices[j] - prices[i]
#                 if diff > max_profit:
#                     max_profit = diff
#                 j+=1
#             i+=1
#         return max_profit
    
    
#DP
# class Solution:
#     def maxProfit(self, prices):
#         max_profit = 0
#         current_profit = 0
        
#         for i in range(1, len(prices)):
#             # Calculate the difference between current and previous price
#             current_profit += prices[i] - prices[i - 1]
#             # If the current profit is negative, reset it to 0
#             current_profit = max(current_profit, 0)
#             # Update the maximum profit
#             max_profit = max(max_profit, current_profit)
        
#         return max_profit
    
    
    #My final solution
class Solution:
    def maxProfit(self, prices):
        min = float('inf')
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < min:
                min = prices[i-1]
            if prices[i] > min:
                max_profit = max(max_profit, prices[i]-min)
        return max_profit

soln = Solution()
print(soln.maxProfit([7,1,5,3,6,4]))
print(soln.maxProfit([7,6,4,3,1]))