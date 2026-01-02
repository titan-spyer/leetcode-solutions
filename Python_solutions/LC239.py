# 239. Sliding Window Maximum
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.
from collections import deque

def maxslidingwindow(nums, k):
    empty = deque()
    ans = []
    for i in range(len(nums)):
        while empty and nums[empty[-1]] < nums[i]:
            empty.pop()
        empty.append(i)
        if empty[0] < i - k + 1:
            empty.popleft()
        if i >= k -1:
            ans.append(nums[empty[0]])
    return ans

print(maxslidingwindow(nums, k))