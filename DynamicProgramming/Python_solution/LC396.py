# LC396: Rotate function.

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Assign the length.
        n = len(nums)

        # Handle the endge case.
        if n == 0 or n == 1:
            return 0

        # Assign two more var for current_f and array_sum.
        current_f = 0
        array_sum = 0

        # Run a loop through the array.
        for i in range(n):
            # Calculate the sum.
            array_sum += nums[i]
            # Calculate the F(0).
            current_f = current_f + (i * nums[i])

        # Assign the max value.
        max_value = current_f

        # Run second loop through the array.
        for k in range(1, n):
            # Identify the last number.
            last = nums[n - k]
            # Calculate the F(k).
            current_f = current_f + array_sum - (n * last)
            # Update the maxmimum.
            max_value = max(max_value, current_f)
        # Return the maximum.
        return max_value