# 560. Subarray Sum Equals K

nums = [1,-1,0]
k = 0

def solution(nums, k):
    i = len(nums)
    ans = 0
    current = 0
    prefix = {0: 1}
    j = 0
    while j < i:
        current += nums[j]
        target = current - k
        if target in prefix:
            ans += prefix[target]
        prefix[current] = prefix.get(current, 0) + 1
        j += 1
            
    return ans


genrated = solution(nums, k)
print(genrated)


ans = 3

if genrated == ans: print(True)
else: print(False)