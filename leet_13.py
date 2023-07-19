#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:27:53 2022

@author: derekfrost
"""
# https://leetcode.com/problems/roman-to-integer/

s = "MCMXCIV"
u = 'LVIII'
t = 'III'
    
roman_dict = {
'I':1,
'IV':4,
'V':5,
'IX':9,
'X':10,
'XL':40,
'L':50,
'XC':90,
'C':100,
'CD':400,
'D':500,
'CM':900,
'M':1000}
    
def roman(s):
    result = 0
    for i,x in enumerate(s):
            if (i+1) == len(s) or roman_dict[x] >= roman_dict[s[i+1]]:
                result += roman_dict[x]
            else:
                result -= roman_dict[x]
    return result
    
    