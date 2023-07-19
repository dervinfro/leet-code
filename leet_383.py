#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 07:01:58 2022

@author: derekfrost
"""

# https://leetcode.com/problems/ransom-note/submissions/

from collections import Counter
a = 'aab'
b = 'baa'
c = 'a'
d = 'b'
e = 'aa'
f = 'ab'
g = 'ba'
h = 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'

def string_compare(x,y):
    # first_str = ''.join(map(str,sorted(x)))
    # second_str = ''.join(map(str,sorted(y)))
    # return first_str in second_str
    result = Counter(x) - Counter(y)
    print(result)
    return not result

