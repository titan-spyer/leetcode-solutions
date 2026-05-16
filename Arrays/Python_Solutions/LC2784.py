# LC2784: Check if Array is Good: https://leetcode.com/problems/check-if-array-is-good/

from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # sort the num.
        nums.sort()
        # Find the length of the num.
        n = len(nums)
        # Loop through the nuums.
        for i in range(n):
            # if nums[number] != the index + 1 .
            if nums[i] != i + 1:
                # return false
                return False
        # if nums last not equal to last index. 
            # return false
        # return true.
        return True