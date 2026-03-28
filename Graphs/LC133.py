
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        visited[node] = Node(node.val, [])

        stack = [node]

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]