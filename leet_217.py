 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:57:14 2023

@author: derekfrost
"""

# nums1 = [1,2,3,1]
# target = 6

# nums2 = [1,2,3,4]
# target = 10
#  https://leetcode.com/problems/contains-duplicate/description/?envType=study-plan&envId=data-structure-i&plan=data-structure

import numpy as np

class DuplicateChecker:
    def check_duplicates(self, nums):
        unique_nums = np.unique(nums)
        return len(unique_nums) != len(nums)

# Example usage:
nums = [1, 2, 3, 4, 5]
checker = DuplicateChecker()
result = checker.check_duplicates(nums)
print(result)  # Output: False

nums1 = [1, 2, 3, 1]
result = checker.check_duplicates(nums)
print(result)  # Output: True


#%%
class Solution:
    def __init__(self) -> None:
        pass
    
    def containsDuplicate(nums) -> bool:
        return len(nums) != len(set(nums))