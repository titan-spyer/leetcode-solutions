from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Edge case to terminate.
        if not grid:
            return 0
        # Define your queue.
        queue = deque()
        # Define variable for fresh count.
        fresh_count = 0
        # Loop through the grid to find the rotten and fresh oranges.
        for i in range(len(grid)):
            for j in range(len(i)):
                # if the orange is rotten add the position to queue.
                if grid[i][j] == 2:
                    queue.append([i, j])
                # elif not rotten increase the fresh count.
                elif grid[i][j] == 1:
                    fresh_count += 1

        # if the fresh count becomes 0.
        if fresh_count == 0:
            # return 0 because it take 0 minute to rotten.
            return 0

        # define your directions.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Define a variable minute to calculate.
        minute = 0
        # Implement the BFS.
            # Define a variable to where to loop on next wave.
            # Loop inside your Queue.
                # At each itration.
                # Loop at each Direction.
                    # If the orange is fresh rotte it.
                    # Add the rotten orange Index to your queue.
                    # Decrease the fresh count.
            # Update your queue with your next wave.
            # If orange rotten possible.
                # Increase the minute.

        # IF there are still fresh orange
            # Return -1.

        # Return the minute.
        pass


def run_test_case(solution: Solution, grid: List[List[int]], expected: int, test_num: int):
    """Helper function to run a single test case and print results"""
    print(f"\n{'='*60}")
    print(f"TEST CASE {test_num}")
    print(f"{'='*60}")
    
    # Print grid in a readable format
    print("Input grid:")
    for row in grid:
        print(f"  {row}")
    
    result = solution.orangesRotting(grid)
    
    print(f"\nOutput: {result}")
    print(f"Expected: {expected}")
    
    if result == expected:
        print(f"\n✅ PASSED")
    else:
        print(f"\n❌ FAILED")
    
    print(f"{'='*60}\n")


def main():
    """Main function to run all test cases"""
    solution = Solution()
    
    # Test case 1: Example from LeetCode - Standard case
    grid1 = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    run_test_case(solution, grid1, 4, 1)
    
    # Test case 2: Example from LeetCode - No fresh oranges
    grid2 = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    run_test_case(solution, grid2, -1, 2)
    
    # Test case 3: Single fresh orange, no rotten
    grid3 = [[1]]
    run_test_case(solution, grid3, -1, 3)
    
    # Test case 4: Single rotten orange
    grid4 = [[2]]
    run_test_case(solution, grid4, 0, 4)
    
    # Test case 5: Empty cell only
    grid5 = [[0]]
    run_test_case(solution, grid5, 0, 5)
    
    # Test case 6: All oranges already rotten
    grid6 = [
        [2,2,2],
        [2,2,2],
        [2,2,2]
    ]
    run_test_case(solution, grid6, 0, 6)
    
    # Test case 7: No rotten oranges, all fresh
    grid7 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    run_test_case(solution, grid7, -1, 7)
    
    # Test case 8: Mixed with walls, all oranges can rot
    grid8 = [
        [2,1,0,1],
        [1,0,1,1],
        [1,1,1,1]
    ]
    run_test_case(solution, grid8, 3, 8)
    
    # Test case 9: 1x5 row - linear spread
    grid9 = [[2,1,1,1,1]]
    run_test_case(solution, grid9, 4, 9)
    
    # Test case 10: 5x1 column - linear spread
    grid10 = [[2],[1],[1],[1],[1]]
    run_test_case(solution, grid10, 4, 10)
    
    # Test case 11: Multiple rotten oranges
    grid11 = [
        [2,1,0,2],
        [1,0,1,1],
        [1,1,1,1]
    ]
    run_test_case(solution, grid11, 2, 11)
    
    # Test case 12: Isolated fresh orange (can't rot)
    grid12 = [
        [2,1,0],
        [0,1,0],
        [0,0,1]
    ]
    run_test_case(solution, grid12, -1, 12)
    
    # Test case 13: Large grid with immediate spread
    grid13 = [
        [2,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1]
    ]
    run_test_case(solution, grid13, 8, 13)
    
    # Test case 14: Rotten oranges in corners
    grid14 = [
        [2,1,0,1,2],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [2,1,0,1,2]
    ]
    run_test_case(solution, grid14, 4, 14)
    
    # Test case 15: Single fresh orange next to rotten
    grid15 = [[2,1]]
    run_test_case(solution, grid15, 1, 15)
    
    # Test case 16: Single fresh orange separated by wall
    grid16 = [[2,0,1]]
    run_test_case(solution, grid16, -1, 16)
    
    # Test case 17: Empty grid (1x1 with 0)
    grid17 = [[0]]
    run_test_case(solution, grid17, 0, 17)
    
    # Test case 18: 3x3 with no solution (fresh orange trapped)
    grid18 = [
        [2,0,1],
        [0,0,0],
        [1,0,1]
    ]
    run_test_case(solution, grid18, -1, 18)
    
    # Test case 19: All walls, no oranges
    grid19 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    run_test_case(solution, grid19, 0, 19)
    
    # Test case 20: Large rectangle with scattered rotten
    grid20 = [
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,2,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,2,1],
        [1,1,1,1,1,1,1,1,1,1]
    ]
    run_test_case(solution, grid20, 8, 20)
    
    # Test case 21: 1x2 grid with both oranges
    grid21 = [[2,1]]
    run_test_case(solution, grid21, 1, 21)
    
    # Test case 22: 1x2 grid with both rotten
    grid22 = [[2,2]]
    run_test_case(solution, grid22, 0, 22)
    
    # Test case 23: 2x2 grid with one rotten, one fresh, one wall, one empty
    grid23 = [
        [2,1],
        [0,0]
    ]
    run_test_case(solution, grid23, 1, 23)
    
    # Test case 24: Complex scenario - BFS order matters
    grid24 = [
        [2,0,1,0,2],
        [1,0,1,0,1],
        [1,1,1,1,1],
        [1,0,1,0,1],
        [2,0,1,0,2]
    ]
    run_test_case(solution, grid24, 4, 24)
    
    print("\n" + "="*60)
    print("ALL TEST CASES COMPLETED")
    print("="*60)


if __name__ == "__main__":
    main()