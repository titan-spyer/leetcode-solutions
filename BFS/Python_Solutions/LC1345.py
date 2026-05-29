# LC1345: Jump Game IV: https://leetcode.com/problems/jump-game-iv/

from typing import List
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Determine the Length.
        n = len(arr)

        # Base Case.
        if n <= 1:
            return 0

        # Build the hash map.
        my_map = defaultdict(list)
        for index, value in enumerate(arr):
            my_map[value].append(index)

        # Assign a Step.
        step = 0
        # Assign a stack to store the jump.
        stack = deque([0])
        # Assign a visited stack.
        visited = set([0])

        # Implement BFS.
        while stack:
            # Determine the length for current step.
            size = len(stack)

            # Process the entire state.
            for _ in range(size):
                curr = stack.popleft()

                # Check if we reach the last index or not.
                if curr == n - 1:
                    return step

                # Teleport to another list.
                next_nodes = [curr - 1, curr + 1] + my_map[arr[curr]]

                for nxt in next_nodes:
                    # can we go to that node.
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)

                # Remove the node from the list.
                del my_map[arr[curr]]

            # Increase the step count.
            step += 1

        return step

answer = Solution()
qes = [100,-23,-23,404,100,23,23,23,3,404]
print(answer.minJumps(qes))