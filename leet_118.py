"""
Author: Derek Frost
Date: July 27, 2023
Leet 118
https://leetcode.com/problems/pascals-triangle/
"""
# This is my code before I pushed my pseudo code to ChatGPT
from itertools import pairwise

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        matrix_sublist = []
        output = []
        array1 = [1]
        array2 = [1 ,1]
        if numRows == 1:
            output = [array1]
            return output
        elif numRows == 2:
            output = [array1, array2]
            return output
        else:
            # Create a FOR loop
            # track the previous array as that will be used for the pairwise 
            # ..in the current array.
            temp1_array = temp_array = array2
            for i in range(3, numRows + 1):    
                matrix = [(x+y) for (x, y) in pairwise(temp_array)]
                new_matrix = temp_array[1:1] = matrix
                matrix_sublist.append(temp
                                      _array)

#%%
from itertools import pairwise

class PascalTriangle:
    # Below is the Class Method decorator
    # The purpose of the decorator is to define a method that operates
    # ..on the class instead of an instance of a class.
    @classmethod
    def generate_triangle(cls, numRows):
        if numRows <= 0:
            return []
        # Set the first level of the Triangle.
        triangle = [[1]]

        for _ in range(1, numRows):
            # This triangle[-1] is the last row of the triangle.
            previous_row = triangle[-1]
            print(previous_row)
            # For each pair in the previous row, pairwise sum the pair
            # ..and add it in between the [1], [1].
            # ..new row is appended to Triangle.
            new_row = [1] + [sum(pair) for pair in pairwise(previous_row)] + [1]
            triangle.append(new_row)

        return triangle

# Example usage:
num_rows = 5
pascal_triangle = PascalTriangle.generate_triangle(num_rows)
print(pascal_triangle)

    
                
                