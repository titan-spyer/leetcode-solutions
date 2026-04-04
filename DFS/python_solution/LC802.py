# LC 802: Find Eventual Safe States

from typing import List

# Solution 1. Robust Time Complexity O(V + E) Space Complexity O(3N)
class Solution:
    # Apply DFS.
    # The function should take current node, list, visited list, path visited, safe node, as argument.
    # The function should return True or False if the Node is safe or not.
    def dfs(self, curr, adj_list, visit, path_visit, is_safe):
        # Make the visit list True.
        visit[curr] = True
        # Make the Path visit to True
        path_visit[curr] = True

        # Loop through the current node list.
        for adj in adj_list[curr]:
            # IF not visited.
            if not visit[adj]:
                # Call the recursive function.
                # If recursive is false.
                if not (self.dfs(adj, adj_list, visit, path_visit, is_safe)):
                    # Return False.
                    return False
            # Else if Path visited.
            elif path_visit[adj]:
                # Return False.
                return False

        # Make it safe node.
        is_safe[curr] = True
        # Make the path visit to 0.
        path_visit[curr] = False
        # Return True.
        return True


    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Detect the length of graph.
        right = len(graph)
        # Create a list visted Node.
        visit = [False] * right
        # Create a list path visit Node.
        path_visit = [False for _ in range(right)]
        # Create a list Safe Node.
        is_safe = [False for _ in range(right)]

        # Run a loop to check each node.
        left = 0
        while left < right:
            # if visited node is 0.
            if not visit:
                # call the DFS.
                self.dfs(left, graph, visit, path_visit, is_safe)
            left += 1

        # Create a answer variable.
        ans = []
        # Run a loop to end of the list.
        left = 0
        while left < right:
            # IF current node is safe.
            if is_safe[left]:
                # Append to result.
                ans.append(left)
            left += 1

        # Return result.
        return ans

# Solution 2: Optimized Time Complexity O(V + E) Space Complexity O(N)
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        right = len(graph)
        # 0 = unvisited, 1 = visiting (in path), 2 = safe
        state = [0] * right 
        
        def dfs(node):
            # If we hit a node that is currently in our path, it's a cycle
            if state[node] == 1:
                return False
            # If we hit a node that we already proved is safe, we are good
            if state[node] == 2:
                return True
                
            # Mark as visiting (add to path)
            state[node] = 1
            
            for adj in graph[node]:
                # If any adjacent node leads to a cycle, this node is not safe
                if not dfs(adj):
                    return False
            
            # If we exit the loop, there are no cycles. Mark as safe.
            state[node] = 2
            return True

        # Run DFS for all nodes and collect the safe ones
        ans = []
        left = 0
        while left < right:
            if dfs(left):
                ans.append(left)
            left += 1
                
        return ans