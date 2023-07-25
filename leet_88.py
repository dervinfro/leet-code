    """
    Leet 88
    https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&envId=data-structure-i&plan=data-structure
    author: Derek Frost
    22 JULY 2023
    """
# Example usage:
array1 = [1, 2, 3, 4]
array2 = [4, 5, 6]
array3 = [1, 2, 3, 0, 0, 0]
array4 = [2, 5, 6]
result = merge_arrays(array1, array2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]


#%%
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        nums1 = (list(filter(lambda x: x != 0, nums1)))
        nums1 = sorted(nums1 + nums2)

        # This was an alternate solution that was provided by Leet Code Solutions
        # ..very similar to what I had...he just put it in one line.
        
        #nums1[:] = sorted(nums1[:m]+nums2)
