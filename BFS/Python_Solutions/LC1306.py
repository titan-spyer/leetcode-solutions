# LC1306: Jump Game III : https://leetcode.com/problems/jump-game-iii/

from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Find the Length of the List.
        n = len(arr)
        # Stack for BFS Algortihm.
        stack = deque([start])

        # Implement the BFS:
        while stack:
            curr = stack.popleft()
            # check if the value is posetive or negative for visited node.
            if arr[curr] < 0:
                continue
            # Edge case to return True.
            if arr[curr] == 0:
                return True
            # Find the value and mark it as visited.
            jump = arr[curr]
            arr[curr] = -jump
            # Check if we can visit the two node of it or not.
            for i in (curr + jump, curr - jump):
                if 0 <= i < n and arr[i] >= 0:
                    stack.append(i)
        return False