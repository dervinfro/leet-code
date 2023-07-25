#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 00:12:08 2022

@author: derekfrost
"""
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""
# https://leetcode.com/problems/two-sum/


nums = [2,7,11,15]
target = 9

# nums = [3,3]
# target = 6

# nums = [2,5,5,11]
# target = 10
#%%
class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       d = {}
       for i, n in enumerate(nums):
           print('i & n: {} {}'.format(i, n))
        # M is the difference between Target and N
           m = target - n
        # If the difference is a Key in the Dictionary, then pass in the Dict Key which returns the index
        # Also...print 'i' which is the index of the current Number/Index pair for the FOR loop.
           if m in d:
               print([d[m], i])
           else:
            # This line is taking the Number as a key and making it equal '=' to the index
               d[n] = i
               print('d: {}'.format(d))

        
Solution().twoSum(nums, target)


