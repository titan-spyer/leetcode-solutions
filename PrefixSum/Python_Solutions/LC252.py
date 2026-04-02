# LC 525: contiguous array
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Define two variable left right
        left = 0
        right = len(nums)
        # define a list to store large value
        seen_value = {0: -1}
        # define another variable to store the large array
        large = 0
        # Define another for sum
        sums = 0
        while left < right:
            if nums[left] == 0:
                sums -= 1
            else:
                sums += 1
            if sums in seen_value:
                curr = left - seen_value[sums]
                if curr > large:
                    large = curr
            else:
                seen_value[sums] = left
            left += 1
        return large