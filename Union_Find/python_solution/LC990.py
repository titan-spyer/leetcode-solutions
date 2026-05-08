# LC 990: https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List

class UnionFind:
    # Define init function
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        # If new email make it parent.
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1

        # Standard method
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()

        for eq in equations:
            if eq[1] == '=':
                uf.union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == '!':
                if uf.find(eq[0]) == uf.find(eq[3]):
                    return False

        return True

# Solution 2
class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        # Create an array of size 26 for 'a' through 'z'
        parent = [i for i in range(26)]
        
        # Path compression is all we need for a max 26-node tree
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
                
        # Pass 1: The Builders (==)
        for eq in equations:
            if eq[1] == '=':
                # Convert string characters to integer indices (0-25)
                x = ord(eq[0]) - 97 
                y = ord(eq[3]) - 97
                union(x, y)
                
        # Pass 2: The Detectives (!=)
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - 97
                y = ord(eq[3]) - 97
                # If they share the same root, we found a paradox
                if find(x) == find(y):
                    return False
                    
        return True