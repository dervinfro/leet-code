#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 08:53:08 2022

@author: derekfrost
"""

# https://leetcode.com/problems/valid-parentheses/

t = "([)]"
u = "{[]}"
def charIsValid(str):
    x = ['()','{}','[]','[]{}','()[]','(){}','()[]{}']
    # return ''.join(sorted(str)) in x
    return str in x

#%%
s = '[}[]'
for i in range(0,len(s),2):
    print(s[i:i+2])
#%%
# def isValid(s):
stack = []
dict = {"]":"[", "}":"{", ")":"("}
for char in u:
    if char in dict.values():
        stack.append(char)
        print('values stack: ', stack)
    elif char in dict.keys():
        print('key char: ', char)
        if stack == [] or dict[char] != stack.pop():
            print('dict char: ', dict[char])
            # return False
            print('False..elif')
    else:
        # return False
        print('False..else')
# return stack == []

#%%
def isValidToo(s):
    stack = []
    dic = {'(': ')', '{':'}', '[':']'}
    for c in s:
        print('stack: ', stack)
        if c in dic:
            stack.append(c)
            print('stack appended: ', c)
        elif not stack: 
            return False
        elif dic[stack.pop()] != c:
            return False
    return not stack

#%% Final Working solution...that I understand
def isValidThree(sequence):
    '''
    Function to check if sequence contains valid parenthesis
    :param sequence: Sequence of brackets
    :return: True is sequence is valid else False
    '''
    # Replace the proper pairs until sequence becomes empty or no pairs are present
    while True:
        if '()' in sequence :
            sequence = sequence.replace ( '()' , '' )
        elif '{}' in sequence :
            sequence = sequence.replace ( '{}' , '' )
        elif '[]' in sequence :
            sequence = sequence.replace ( '[]' , '' )
        else :
            return not sequence
        
#%%

def isValid(s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            print('C: ', c)
            if c in mapping: 
                stack.append(c)
                print('Stack: ', stack)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]
