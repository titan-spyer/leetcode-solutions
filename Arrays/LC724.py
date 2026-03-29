# LC 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        right_sum = 0
        left = 0
        right = len(nums)
        while left < right:
            right_sum = total - left_sum - nums[left]
            if left_sum == right_sum:
                return left
            left_sum += nums[left]
            left += 1
        return -1
            