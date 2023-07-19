#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 23:54:57 2022

@author: derekfrost
"""
# https://leetcode.com/problems/capitalize-the-title/submissions/

x = 'lotion on the skin'
y = "L hV"

# List Comprehension with multiple conditions.
# Take in a string and change each word (> than 2) to a capitalized word.
class Solution:
    def capitalizeTitle(self, title:str):
        return ' '.join([w.lower() if len(w) <= 2 else w.title() for w in title.split()])
