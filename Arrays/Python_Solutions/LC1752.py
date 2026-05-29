# LC1752 : check if array is sorted and rotated. : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List
from collections import deque

class Solution:
    def check(self, nums: List[int]) -> bool:
        array = deque(nums)
        nums.sort()
        if nums == list(array):
            return True
        for i in range(len(nums)):
            array.appendleft(array.pop())
            if nums == list(array):
                return True
        return False
    # Pythonic solution.
        return sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums))) <= 1

answer = Solution()
qes = [3,4,5,1,2]
print(answer.check(qes))