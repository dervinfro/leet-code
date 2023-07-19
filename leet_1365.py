#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:07:28 2022

@author: derekfrost
"""

nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

output = [i for i in nums if i < nums[4]]

output1 = []
throwaway_list = []

for index, num in enumerate(nums):
    for i in nums:
        if i < nums[index]:
            throwaway_list.append(i)
    output1.append(len(throwaway_list))
    throwaway_list.clear()
    
    
    
indices = {}
for idx, num in enumerate(sorted(nums)):
    indices.setdefault(num, idx)
final = [indices[num] for num in nums]