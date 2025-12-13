target, nums = 7, [2,3,1,2,4,3]

def subarray(target, nums):
    left = 0
    wsum = 0
    ans = float('inf')

    for r in range(len(nums)):
        wsum += nums[r]

        while wsum >= target:
            ans = min(ans, (r - left + 1))
            wsum -= nums[left]
            left += 1

    if ans == float('inf'):
        return 0
    return ans


print(subarray(target, nums))
