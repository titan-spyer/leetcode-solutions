# LC1914: Cyclically Rotating a Grid : https://leetcode.com/problems/cyclically-rotating-a-grid/

from typing import List

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        layers = min(rows, cols) // 2

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        for _ in range(layers):
            # PHASE 1: Map the Coordinates of the Ring
            coords = []
            
            # Top edge (Left to Right, inclusive)
            for c in range(left, right + 1): 
                coords.append((top, c))
                
            # Right edge (Top+1 to Bottom, inclusive)
            for r in range(top + 1, bottom + 1): 
                coords.append((r, right))
                
            # Bottom edge (Right-1 down to Left, inclusive)
            for c in range(right - 1, left - 1, -1): 
                coords.append((bottom, c))
                
            # Left edge (Bottom-1 up to Top+1)
            for r in range(bottom - 1, top, -1): 
                coords.append((r, left))


            # PHASE 2: Extract & Shift using List Comprehensions
            # Instantly pull all values using our coordinate map
            ring_vals = [grid[r][c] for r, c in coords]
            
            # Rotate counter-clockwise
            k_mod = k % len(ring_vals)
            shifted_vals = ring_vals[k_mod:] + ring_vals[:k_mod]


            # PHASE 3: Reroll the shifted array back to 2D
            # zip() ties our coordinate map and our new values together perfectly
            for (r, c), val in zip(coords, shifted_vals):
                grid[r][c] = val


            # PHASE 4: Shrink the boundaries
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return grid

answer = Solution()

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

k = 2

print(answer.rotateGrid(grid, k))