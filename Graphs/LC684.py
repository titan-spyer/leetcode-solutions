# LC 684: Redundant Connection.
from typing import List
class UnionFind:
    def __init__(self, n):
        # Create the arrays.
        self.parent = [i for i in range(n + 1)] 
        self.rank = [1] * (n + 1)
    def find(self, n):
        # If I am not the ultimate boss...
        if self.parent[n] != n:
            # ...recursively find the boss, and plug myself DIRECTLY into them (Path Compression)
            self.parent[n] = self.find(self.parent[n])
            
        return self.parent[n]
    def union(self, n1, n2):
        # 1. Find the ultimate bosses
        root1 = self.find(n1)
        root2 = self.find(n2)
        
        # 2. CYCLE DETECTED! They are already in the same network.
        if root1 == root2:
            return False 
            
        # 3. MERGE: The smaller rank reports to the larger rank
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2] # Update the size of the winning company
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]
            
        return True # Successfully merged
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            n = len(edges)
            uf = UnionFind(n)

            for u, v in edges:
                if not uf.union(u, v):
                    return [u, v]