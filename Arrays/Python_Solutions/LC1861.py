# LC1861: Rotating the Box: https://leetcode.com/problems/rotating-the-box/

from typing import List

Solution 1 time complexity O(m x n) space complexity O(m x n)
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Solve it in two phase.
        # calculate the list length.
        n = len(boxGrid[0]) 
        # First phase move the stone to empty spot.
        for row in boxGrid:
        # Assign a variable for empty spot.
            empty = n - 1
            for j in range(n -1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    # swap the value.
                    row[j], row[empty] = '.' '#'
                    empty -= 1

        # Loop through the matrix
        # Second Phase rotate the matrix.
        boxGrid = [list(row[::-1]) for row in zip(*boxGrid)]
        return boxGrid

answer = Solution()
grid = [["#",".","*","."], ["#","#","*","."]]
print(answer.rotateTheBox(grid))