#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:14:35 2022

@author: derekfrost
"""

#https://leetcode.com/problems/valid-anagram/submissions/
"""
Determine if two strings are anagrams of each other.
"""
from collections import Counter

s = "anagram"
t = "nagaram"

def anagram(s,t):
    return Counter(t) == Counter(s)



