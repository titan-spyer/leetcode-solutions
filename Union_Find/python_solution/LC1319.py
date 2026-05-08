# LC 1319: Number of Operations to Make Network Connected

from typing import List

# Class for UnionFind.
class UnionFind:
    def __init__(self, n: int):
        # Create the Arrays.
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, n):
        # Check if it is the Highest rank.
        if self.parent[n] != n:
            # If not Use resursion to find the highest rank and plug it to current.
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        # Cycle Detected.
        if root1 == root2:
            return False

        # Merge the smaller to Larger.
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]

        return True

connections = [[0,1],[0,2],[1,2]]
n = 4
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''I have to design something using Union find that if it found any parent connection between two nodes it won't connect that nodes
        increase the available node count by 1 and at the end check  if the remain cable can connect to rest of the device'''
        '''
        Conncet the all computers with limited given cabels (Union Find)

        Parameters:
        n: The number of Computers
        connections: The connceted list each node have two connection between two computer

        return: the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
        '''
        # if n - 1 is greater than the connections.length.
        if len(connections) < n -1:
            # return -1. (Not enough edge to connect)
            return -1
        # Calculate the Count
        uf = UnionFind(n)
        c_componet = n

        for u, v in connections:
            if uf.union(u, v):
                c_componet -= 1

        # Return connected component - 1
        return c_componet  - 1