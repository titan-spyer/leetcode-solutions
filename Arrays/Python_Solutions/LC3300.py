# LC3300: Minimum Element after replacement of digit sum : https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:        
        str_list = list(map(str, nums))
        k = 0
        for i in str_list:
            sum = 0
            for j in i:
                sum += int(j)
            nums[k] = sum
            k += 1
        nums.sort()
        return nums[0]

answer = Solution()
qes = [999,19,199]
print(answer.minElement(qes))