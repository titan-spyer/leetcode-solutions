# LC1462: Course Schdule iv

from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Define a Dictonary to store the course and it's prerequisties.
        courses = {i: [] for i in range(numCourses)}
        # Define a indegree to store course that don't have prerequisties.
        indegree = [0] * numCourses

        # Run a loop to add prerequisites to courses and also indegrees.
        left = 0
        right = len(prerequisites)
        while left < right:
            # Add the courses to it's prerequisties. {prerequisties: courses}
            courses[prerequisites[left][0]].append(prerequisites[left][1])
            # Add the indegree value and increase it if certain course have more number of prerequistes
            # Ex index is the courses and values is it's prerequisties count.
            indegree[prerequisites[left][1]] += 1
            left += 1

        # Define a queue to add the indegree = 0 value.
        queue = deque()
        # Run a loop to add the 0 indegree value to queue.
        left = 0
        while left < numCourses:
            if indegree[left] == 0:
                queue.append(left)
            left += 1

        # implement a Cache to store the prerequisites value that accesable
        cache = [set() for _ in range(numCourses)]

        # Implement BFS.
        while queue:
            curr = queue.popleft()


            for u_c in courses[curr]:
                # 1. Add the direct prerequisite
                cache[u_c].add(curr)
                # 2. Add ALL indirect prerequisites (The Magic Step!)
                cache[u_c].update(cache[curr])


                indegree[u_c] -= 1
                if indegree[u_c] == 0:
                    queue.append(u_c)

        ans = []
        for u, v in queries:
            if u in cache[v]:
                ans.append(True)
            else:
                ans.append(False)

        return ans