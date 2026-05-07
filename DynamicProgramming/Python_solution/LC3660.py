# LC 3660: Jump game xi : https://leetcode.com/problems/jump-game-ix/

from itertools import accumulate
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # Solve in two phase.
        # Determine the length of the nums.
        length = len(nums)

        # First phase determine the maximum prefix.
        max_prefix = list(accumulate(nums, max))

        # Second Phase store the sum while calculating the minimum so far.
        # Initial a larger value to store the minimum value.
        min_far = float('inf')

        # Initial the answer array.
        answer = [0] * length
        # Run a loop in backward direction.
        for i in range(length - 1, -1, -1):
            # if i+1 is allowed and max_prefix is greater than the min_suffix + 1.
            if ((i + 1) < length ) and max_prefix[i] > min_far:
                # ans should be ans + 1.
                answer[i] = answer[i + 1]
            # else ans should be the max_prefix
            else:
                answer[i] = max_prefix[i]

            min_far = min(min_far, nums[i])
        return answer

answ = Solution()
nums = [2,1,3]
print(answ.maxValue(nums))