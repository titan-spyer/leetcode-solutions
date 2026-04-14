# LC310: https://leetcode.com/problems/minimum-height-trees/

from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Handeling Edge cases.
        if n <= 2:
            return [i for i in range(n)]

        # Define storage for your BFS.
        graph = {i: [] for i in range(n)}
        indegree = [0] * n

        # Find the connection between node.
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1
            indegree[u] += 1

        # Add value to queue to run the bfs.
        queue = deque()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)

        # BFS loop.
        while queue:
            # Return the list if less than 2 it means reach the mid point.
            if n <= 2:
                return list(queue)

            # Take the snapshot each time to run your loop and remove the node from total.
            size = len(queue)
            n -= size

            # Run your snap.
            for _ in range(size):
                curr = queue.popleft()
                # BFS khan's alogrithm for BFS.
                for u in graph[curr]:
                    indegree[u] -= 1
                    if indegree[u] == 1:
                        queue.append(u)

        # Return the final list.
        return list(queue)


def run_test_case(solution: Solution, n: int, edges: List[List[int]], expected: List[int], test_num: int):
    """Helper function to run a single test case and print results"""
    print(f"\n{'='*60}")
    print(f"TEST CASE {test_num}")
    print(f"{'='*60}")
    print(f"Input: n = {n}")
    print(f"Edges: {edges}")
    
    result = solution.findMinHeightTrees(n, edges)
    
    print(f"\nOutput: {result}")
    print(f"Expected: {expected}")
    
    # Sort both for comparison since order doesn't matter
    result_sorted = sorted(result) if result else []
    expected_sorted = sorted(expected) if expected else []
    
    if result_sorted == expected_sorted:
        print(f"\n✅ PASSED")
    else:
        print(f"\n❌ FAILED")
    
    print(f"{'='*60}\n")


def main():
    """Main function to run all test cases"""
    solution = Solution()

    # Test case 5: Four nodes in a line
    run_test_case(solution, 4, [[0,1],[1,2],[2,3]], [1,2], 5)
    
    # Test case 1: Single node
    run_test_case(solution, 1, [], [0], 1)
    
    # Test case 2: Two nodes connected
    run_test_case(solution, 2, [[0,1]], [0,1], 2)
    
    # Test case 3: Three nodes in a line
    run_test_case(solution, 3, [[0,1],[1,2]], [1], 3)
    
    # Test case 4: Star pattern with 4 nodes
    run_test_case(solution, 4, [[0,1],[0,2],[0,3]], [0], 4)
    
    
    # Test case 6: Balanced tree with 6 nodes
    run_test_case(solution, 6, [[0,1],[0,2],[1,3],[1,4],[2,5]], [0,1], 6)
    
    # Test case 7: Six nodes in a line
    run_test_case(solution, 6, [[0,1],[1,2],[2,3],[3,4],[4,5]], [2,3], 7)
    
    # Test case 8: Perfect binary tree with 7 nodes
    run_test_case(solution, 7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [0], 8)
    
    # Test case 9: Complex tree
    run_test_case(solution, 8, [[0,1],[0,2],[0,3],[3,4],[4,5],[4,6],[4,7]], [3], 9)
    
    # Test case 10: Large linear chain (10 nodes)
    edges_10 = [[i, i+1] for i in range(9)]
    run_test_case(solution, 10, edges_10, [4,5], 10)
    
    # Test case 11: Star pattern with 5 nodes
    run_test_case(solution, 5, [[0,1],[0,2],[0,3],[0,4]], [0], 11)
    
    # Test case 12: Two connected components? (Invalid per problem constraints, but testing edge case)
    # Note: Problem guarantees tree (connected, no cycles), so this won't happen, but good to test
    run_test_case(solution, 4, [[0,1],[2,3]], [], 12)  # Should handle gracefully
    
    # Test case 13: n=1 with self-loop? (Invalid, but testing)
    run_test_case(solution, 1, [[0,0]], [0], 13)  # Should handle or ignore self-loop
    
    # Test case 14: Empty edges with n=3 (disconnected - invalid tree)
    run_test_case(solution, 3, [], [], 14)
    
    print("\n" + "="*60)
    print("ALL TEST CASES COMPLETED")
    print("="*60)


if __name__ == "__main__":
    main()