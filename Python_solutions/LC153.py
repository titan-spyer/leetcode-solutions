# 153. Find Minimum in Rotated Sorted Array
nums = [2,3,4,5,6,7,1]

def answer(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if l == r:
            return nums[l]
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] <= nums[r]:
            r = m
    return nums[l]

print(answer(nums))