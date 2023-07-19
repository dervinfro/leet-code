#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:36:28 2022

@author: derekfrost
"""
# https://leetcode.com/problems/palindrome-number/submissions/

x = 121
y = -121
z = 123

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)