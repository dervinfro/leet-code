#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 00:32:59 2022

@author: derekfrost
"""
from itertools import groupby

# This is just a funky way of splitting up a list
x = [1,2,2,2,3,4,5,6]
x[2:] + x[:2]
#%%
# Remove all occurances of element from a list
while 2 in x:
    x.remove(2)
print(len(x))
    
#%%
"""
Create a Class with a Method.
In that method, use itertools groupby function.
Groupby function will return a list for each consecutive number of chars.
Take the len of each list and pass it as a condition to the previous list.
If greater, then set as a var in listAppend.
"""
# https://leetcode.com/problems/consecutive-characters/submissions/

s = "leetcode"
ss = "abbcccddddeeeeedcba"

class Solution:
    def maxPower(self, s: str) -> int:
        listAppend = 0
        for k,g in groupby(s):
            list_g = list(g)
            if len(list_g) > listAppend:
                listAppend = len(list_g)
            else:
                pass
        print('List value: ', listAppend)