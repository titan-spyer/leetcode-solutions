# LC: 2270. Number of Ways to Split Array

qes = [10,4,-8,7]

def solution(nums):
    # Version 2
    total = sum(nums)
    value = 0
    ans = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        value += nums[left]
        if value >= (total - value):
            ans += 1
        left += 1
    return ans



genrated = solution(qes)
print(genrated)


ans = 2

if genrated == ans: print(True)
else: print(False)