#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:23:34 2022

@author: derekfrost
"""
# https://leetcode.com/problems/reverse-string/
s = ["h","e","l","l","o"]

start = 0
end = len(s) - 1

while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1
    
print(s)