# LC 721: Accounts Merge.

from typing import List
import collections


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
'''For simplification take the input as
accounts = [['parent', "child1", "child2"], ['parent', "child1", "child2"],...]
we have to check if both child belongs to same parent merge them and add to answer because answer can be any order'''
ans = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# PreRequisties
# UnionFind: TO find the link between two list
# String: To perform the Operation
# Binary Search: to compare between each element

# Define Your UnionFind class.
'''To you are given two list you have to skip the first element of each list and compare rest of the elemnt if match found return True'''
# Define the class.
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Implement Binary Search on the list to compare between elements in parent list.
        # Provide two list to the union it will compare with it's elements
        # if it returns true merge them and add to result.
        uf = UnionFind()
        e_m_t_n = {}

        for account in accounts:
            name = account[0]
            anch_email = account[1]
            left = 1
            right = len(account)
            while left < right:
                email = account[left]

                uf.union(anch_email, email)

                e_m_t_n[email] = name
                left += 1

        merged_mails = collections.defaultdict(list)

        for email, emails in e_m_t_n:
            root = uf.find(email)
            merged_mails[root].append(email)

        ans = []
        for root_mail, emails in merged_mails.items():
            name = e_m_t_n[root_mail]
            sorted_mails = sorted(emails)
            ans.append([name] + sorted_mails)

        return ans