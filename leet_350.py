"""
Author: Derek Frost
Date: 24 JUL 2023
Leet 350
https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=study-plan&envId=data-structure-i&plan=data-structure
"""
    
from collections import Counter

array1 = [1, 2, 2, 1]
array2 = [2, 2]
array3 = [1,3,4,5,6,6,8]
array4 = [3,5,6]

set(array1).intersection([2,2])

for x in range(len(array1) - 1):
    array2 == [array1[x], array1[x + 1]]
    
for x in range(len(array1)):
    array2 == array1[:x + 1]
    
a1 = Counter(array1)
a2 = Counter(array2)
a3 = Counter(array3)
a4 = Counter(array4)
a3 = a1 & a2
print(list(a3.elements()))