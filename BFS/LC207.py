# LC 207: Course Schedule.
from collections import deque

prerequisites = [[1,0]]
numCourses = 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Define a dictonary to store the courses and it's prerequisites
        courses = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        # Loop through the graph and find the prerequisites and add to dictonary
        # First Phase
        right = len(prerequisites)
        left = 0
        while left < right:
            # Also add the values which don't have prerequisites in a queue
            courses[prerequisites[left][1]].append(prerequisites[left][0])
            indegree[prerequisites[left][0]] += 1
            left += 1
        left = 0
        queue = deque()
        while left < numCourses:
            if indegree[left] == 0:
                queue.append(left)
            left += 1
        course_taken = 0
        # Loop until the number of courses left
        while queue:
            # remove the no dependency course from the queue
            curr = queue.popleft()
            course_taken += 1
            # check if any dictonary value is gonna empty or not
            for u_c in  courses[curr]:
                indegree[u_c] -= 1
                if indegree[u_c] == 0:
                    queue.append(u_c) 
        # if dictonary contain value after loop then return False if not then True
        return numCourses == course_taken
