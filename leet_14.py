#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:48:07 2022

@author: derekfrost
"""
# https://leetcode.com/problems/longest-common-prefix/
x = 'iamastring'
y = ['true','truth','truffle']
z = ['stop','drop','roll']
a = ["flower","flow","flight"]
b = ['a']



def compare_strings(strs):
    strs.sort()
    min_word = min(len(strs[0]), len(strs[-1]))
    for i in range(min_word):
        if strs[0][0:i] == strs[-1][0:i]:
            result = strs[0][0:i]
            print(result)
        elif strs[0][0:1] != strs[-1][0:1]:
            result = ''
    return result

#%%

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result=''
        if len(strs)==0:
            return result
        strs.sort()
        for i in range(len(min(strs))):
            if strs[0][0:i+1] == strs[-1][0:i+1]:
                # print(strs[0][0:i+1])
                result = strs[0][0:i+1]
            else:
                break
        return result
