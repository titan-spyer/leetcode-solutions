# LC 210: Course Schedule.
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Define a Dictonary to store it's prerequisties.
        courses = {i: [] for i in range(numCourses)}
        # Define a indegree to store the course that can taken without prerequisites.
        indegree = [0] * numCourses

        # First Phase: add the prerequisites.
        # Implement a loop to add the prerequisties
        right = len(prerequisites)
        left = 0
        while left < right:
            # Add the prerequisites.
            courses[prerequisites[left][1]].append(prerequisites[left][0])
            # Add the indegree.
            indegree[prerequisites[left][0]] += 1
            left += 1

        # Second Phase: add the indegree value to queue.
        # Define a queue.
        queue = deque()
        # Implement  a loop to add value to queue.
        left = 0
        while left < numCourses:
            # Check if the prerequesties is 0.
            if indegree[left] == 0:
                # Add the Value to queue.
                queue.append(left)
            left += 1

        # Third Phase: Implement the BFS.
        # Implement a List to add the order.
        answer = []
        # While queue.
        while queue:
            # Pop an element from left.
            curr = queue.popleft()
            # Add it to the List.
            answer.append(curr)
            # Run a loop to find reduce the course for an prerequistes.
            for u_c in courses[curr]:
                # Reduce the Value in indgree.
                indegree[u_c] -= 1
                # If the indegree become 0.
                if indegree[u_c] == 0:
                    # Add it to the queue.
                    queue.append(u_c)

        # Return the List.
        if len(answer) == numCourses:
            return answer
        else:
            return []
