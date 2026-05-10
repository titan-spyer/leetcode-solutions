# LC 2770 : Maximum number of jumps to reach the last index: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # Calculate the length of list.
        n = len(nums)

        # Initial a list of -1 to store the each iteration value.
        dp = [-1] * n
        # Base case for first index.
        dp[0] = 0

        # Run outer loop through the list.
        for i in range(n):
            # Define a condition to skip unreachable values.
            if dp[i] == -1:
                continue

            # Run an inner loop start from outer loop to calculate each time value.
            for j in range(i + 1, n):
            # check if the jump is valid or not.
                if abs(nums[j] - nums[i]) <= target:
                    # store the maximum of it.
                    dp[j] = max(dp[j], dp[i] + 1)
        # Return the maximum.
        return dp[-1]
