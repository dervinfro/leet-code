#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 23:31:51 2022

@author: derekfrost
"""
"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. If no such two words exist, return 0.
"""
# 318. Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/
from itertools import combinations


z = ['stop','drop','roll','gib']
a = ["a","ab","abc","d","cd","bcd","abcd"]
b = ['a', 'ab', 'abc', 'abcd']


class Solution:
    def maxProduct(self, words: list[str]) -> int:
         # return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) & set(s2))], default=0)
         result=[0]
         for s1, s2 in combinations(words, 2):
             if not (set(s1) & set(s2)):
                 result.append(len(s1) * len(s2))
         return max(result)
