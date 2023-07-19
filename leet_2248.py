#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:22:10 2022

@author: derekfrost
"""
# https://leetcode.com/problems/intersection-of-multiple-arrays/submissions/

# NOTE: the * is a 'starred expression' used for unpacking 
class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        return sorted(set.intersection(*map(set,nums)))