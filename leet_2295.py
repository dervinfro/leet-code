#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 00:21:13 2022

@author: derekfrost
"""

# https://leetcode.com/problems/replace-elements-in-an-array/

# nums = [1,2,4,6]  # Should change to: [3,2,7,1]
# operations = [[1,3],[4,7],[6,1]]
# dict_operations = {1: 3, 4: 7, 6: 1}

nums = [1,2]  # Should change to [2,1]
operations = [[1,3],[2,1],[3,2]]
dict_operations = {1: 3, 2: 1, 3: 2}
#%%
"""
Convert List to Dictionary using the List values as Keys and the Index as Values.
Use the Dictionary.get() method to match dictionary keys to the 1st integer in the list value pair.
NOTE: .get() will ONLY return matches.  If .get() is passed a value that is not in 
..the dict keys, then no index value will be returned.


"""
print('Nums List: ', nums)
seen = {}  
for i in range(len(nums)):  # < - This is the move right here.....using len to create an index for a dict.
    seen[nums[i]] =  i  # Key/Value set to: {1: 0, 2: 1}
print('Seen Dictionary: ', seen)

for i in range(len(operations)):
    print('Operations[i][0]: ', operations[i][0])  # Returns: 1,2,3
    
    idx = seen.get(operations[i][0])  # Returns the Value: (0 & 1) from the Key/Value pair: {1: 0, 2: 1}
    print('Index from seen.get(): ', idx)
    
    nums[idx] = operations[i][1]
    print('Nums: ', nums)
    print('Seen Dictionary BEFORE .pop(): ', seen)
    
    print('Operations[i][0]: ', operations[i][0])
    seen.pop(operations[i][0])
    print('Seen Dictionary AFTER .pop(): ', seen)
    
    seen[operations[i][1]] = idx
    print('Seen Dictionary after new index: ', seen)
    
print(nums)

#%%
"""
Create FOR loop to read all of the Keys from a copy of the dictionary.
Condition: if Keys are in nums List
- if the Keys are in the List, then run the dictionary .get() against any given Key.
- from this...return the Key to the nums index NESTED inside the nums List Indexing method
Remove the Key/Value from the dictionary that matches the Key (k) passed into the .pop() method

NOTE: One of the reaons why this works is that the nums List is already pre-populated.  I just  
..determine if an integer in nums List matches any of the Keys in the Dictionary.
If this is True...great....set the nums List Index to the dictionary.get(k).
If this is False...pass.  I can do this because my non-matching values are already in the nums List.

"""
def replaceElements(nums, operations):
    dict_operations = dict(operations)
    for k in dict_operations.copy():  # List out the Keys of the Dictionary
        if k in nums:   # Are any of the Keys in the List?
            print(f'first k value {k}')
            nums[nums.index(k)] = dict_operations.get(k)  # If TRUE, set the nums k index to the value of the dictionary .get() Value
            dict_operations.pop(k)  # Remove the Key/Value pair from the Dictionary where the Key is == k
            print(f'the dictionary after a .pop() {dict_operations}')
        else:
            # print(f'this is a k value that fell within the ELSE condition {k}')
            pass
            
    print(f'this is the final output for nums {nums}') 
    return nums     
        
replaceElements(nums, operations)
        

    