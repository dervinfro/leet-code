"""
Date: JULY 25, 2023
Author: Derek Frost
Leet: 121
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description
"""

from itertools import pairwise, combinations

array1 = [7, 5, 1, 9]
prices = [7,6,4,3,1]

array_max = max((y-x) for (x, y) in pairwise(prices))
print(max(0, array_max))

array_max1 = max([(y-x) for (x,y) in combinations([1], 2)], default=0)
print(max(0, array_max1))

#%%

def biggest_future_diff(*args):
    max_difference = 0 

    # Create a nested FOR loop
    for i in range(len(args)):
        current_value = args[i]
        
        for j in range(i+1, len(args)):
            future_value = args[j]
            difference = current_value - future_value
            
            if difference > max_difference:
                max_difference = difference
                
    return max_difference

#%%
class Solution:
    def maxProfit(self, prices: list[int]) -> int:                           
        mn, mx = prices[0], 0
        print('mn mx:', mn, mx)             
                                           
        for p in prices:    
            print('p: ', p)                                                          
            if   p < mn     : 
                mn = p 
                print('mn: ', mn)  
            elif p > mx + mn: 
                mx = p - mn  
                print('mx: ', mx)
        return mx                           
# %%
import itertools
for (x,y) in itertools.pairwise(array1):
    print(x,y)
