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
           m = target - n
           if m in d:
               print([d[m], i])
           else:
               d[n] = i

        
Solution().twoSum(nums, target)


