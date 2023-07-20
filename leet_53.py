""" 
July 20, 2023
Derek Frost
https://leetcode.com/problems/maximum-subarray/description/
Problem 53
"""

nums = [-1,2,3,-2,4,-7]

# Define Class
# NOTE: Class does not have __init__ method as it is not required.
# If I did pass in the __init__, I would not be required to pass in the parens (ie Solution vs. Solution())
# NOTE: There are no Class Attributes and no Instance Variables.
class Solution:
    # Define the Method using 'self' to represent the instance of the Class
    # The first arguement of every Method is 'self'
    # Second arguement is nums list, which will return an int.
    def maxSubArray(self, nums: list[int]) -> int:
        # Set both maxSum and currentSum to 0...we are only looking for the SUM of an array
        # Were never looking for an array with a sum of 0.  The final array will always be a positive integer
        maxSum = currentSum = 0
        # Loop through the entire range of the nums list
        for num in nums[:]:
            # This is where it took some digging on my end.
            # The currentSum + num is the running total for each paired elements in the array
            # So we either take the Max of the element or the running total...and pass that along
            # Then...we either take the previous maxSum or the currentSum...whichever is greater
            # That maxSum is what keeps the MAX running total...which is returned when the loop ends.
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        return maxSum
        
