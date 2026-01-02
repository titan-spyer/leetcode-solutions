# 33. Search in Rotated Sorted Array
nums = [6,7,1,2,3,4,5] 
target = 3

def solution(nums, target):
    l, r = 0, len(nums) -1
    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return m
        # check if left half is sorted.
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        # Check if right half is sorted.
        elif nums[m] <= nums[r]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

print(solution(nums, target))