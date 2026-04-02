# LC 994: Rotting Oranges.
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # First Phase: Detecting Rotten Oranges.
        # Implement a queue.
        queue = []
        # Implement a fresh orange counter.
        fresh_count = 0
        # Run a nested loop to run through the Grid.
        left, row, col = 0, len(grid), len(grid[0])
        while left < row:
            col_left = 0
            while col_left < col:
                # Detect the rotten orange and add it to queue.
                if grid[left][col_left] == 2:
                    queue.append((left,col_left))
                # Detect the Fresh orange and increment the fresh orange count.
                elif grid[left][col_left] == 1:
                    fresh_count += 1
                col_left += 1
            left += 1

        # Check for 0 Minute.
        if fresh_count == 0:
            return 0

        # Second Phase: rotting the oranges.
        # Implement the direction [(-1, 0), (1, 0), (0, -1), (0, 1)].
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Implement a minute count.
        minute_count = 0
        # Implement the BFS.
        # While queue.
        while queue:
            # Detect the current Wave size for the snapshot.
            next_wave = []
            # Implement Another Loop to run through the snap preiod.
            for x, y in queue:

                # Go in each direction.
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < row and 0 <= ny < col:
                        # Make other orange rotten.
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh_count -= 1
                            # Add the rotten oranges to queue.
                            next_wave.append((nx, ny))
            queue = next_wave
            # Increase the minute Count.
            if queue:
                minute_count += 1

        # Third Phase: Detecting the fresh Oranges.
        # if fresh orange > 0:
        if fresh_count > 0:
            # Return -1
            return -1
        # Return the minute count.
        return minute_count