# LC2553: Separate the digits in an array : https://leetcode.com/problems/separate-the-digits-in-an-array/

from typing import List
from collections import deque


# C++ type Solution 
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = deque()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            while nums[i] != 0:
                answer.appendleft((nums[i]%10))
                nums[i] //= 10
        return list(answer)

# Python type solution.
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]

answer = Solution()
qes = [13,25,83,77]
print(answer.separateDigits(qes))