# LC1340: JUMP GAME V. : https://leetcode.com/problems/jump-game-v/

from typing import List
from functools import cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Calculate the len.
        n = len(arr)
        # Use the python cache tool for memory mapping.
        @cache
        # DFS(i)
        def dfs(i: int) -> int:
            # assign the max jumps variable.
            max_jump = 1
            # loop through the posetive index.
            for j in range(1, d+1):
                # find the next index.
                next_i = i + j
                # check if the jump is possible or not.
                if next_i >= n or arr[next_i] >= arr[i]:
                    break
                # find the max jumps.
                max_jump = max(max_jump, 1 + dfs(next_i))
            # Loop through the negative index.
            for j in range(1, d+1):
                # Find the next index.
                next_i = i - j
                # Check if the jump is possible or not.
                if next_i < 0 or arr[next_i] >= arr[i]:
                    break
                # Find the max jumps.
                max_jump = max(max_jump, 1 + dfs(next_i))
            # Return the max jumps.
            return max_jump
        #  return the maximum.
        return max(dfs(i) for i in range(n))
