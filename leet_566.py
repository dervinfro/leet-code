"""
Author: Derek Frost
Date: July 25, 2023
Leet 566
https://leetcode.com/problems/reshape-the-matrix/
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
#%%
my_list = [1, 2, 3, 4, 5,
		6, 7, 8, 9]
start = 0
end = len(my_list)
step = 3
for i in range(start, end, step):
    x = i
    print(i, i+step)
    
    
#%%
def reshape_matrix(matrix, new_rows, new_columns):
    # Check if the new shape is valid
    original_rows = len(matrix)
    original_columns = len(matrix[0])
    original_elements = original_rows * original_columns
    new_elements = new_rows * new_columns

    if original_elements != new_elements:
        raise ValueError("New shape should have the same number of elements as the original matrix.")

    # Flatten the original matrix into a 1D list
    flattened_matrix = sum(matrix, [])

    # Create the reshaped matrix with the specified shape
    reshaped_matrix = [flattened_matrix[i:i + new_columns] for i in range(0, new_elements, new_columns)]

    return reshaped_matrix

# Example usage:
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

new_rows = 1
new_columns = 12

result = reshape_matrix(original_matrix, new_rows, new_columns)
print(result)


# %%
for x in range(0,11,6):
    print(result[0][x:x+6])
# %%
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        original_elements = row * col
        new_elements = r * c
        if original_elements != new_elements:
            print('pass')
            pass
        else:
            flat_matrix = sum(mat, [])
            mat = [flat_matrix[i:i+c] for i in range(0, new_elements, c)]

        return mat
# %%
