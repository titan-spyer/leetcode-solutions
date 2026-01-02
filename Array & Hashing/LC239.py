# 239. Sliding Window Maximum
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

def maxslidingwindow(nums, k):
    ans = []
    for i in range(len(nums) - 2):
        j = 0
        l = i
        a = nums[i]
        while j < k - 1:
            a = max(a, nums[l + 1])
            l += 1
            j += 1
        # a = max(nums[i], nums[i + 1], nums[i + 2])
        ans.append(a)
    return ans

print(maxslidingwindow(nums, k))