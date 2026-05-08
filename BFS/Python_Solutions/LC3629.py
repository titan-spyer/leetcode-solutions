# LC3629: Minimum Jumps to Reach end via Prime Teleportation: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge case
        if n == 1:
            return 0

        # Build Smallest Prime Factor Sieve
        max_val = max(nums)
        spf = list(range(max_val + 1))

        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:  # prime
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Function: Get Unique Prime Factors
        def get_prime_factors(x):
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x //= spf[x]
            return factors

        # Build Prime Buckets
        buckets = defaultdict(list)
        for i in range(n):
            factors = get_prime_factors(nums[i])
            for p in factors:
                buckets[p].append(i)

        # BFS
        queue = deque([0])
        visited = set([0])

        jumps = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()

                # Reached destination
                if curr == n - 1:
                    return jumps

                # Move Left / Right
                for nxt in [curr - 1, curr + 1]:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                # Prime Factor Teleportation
                val = nums[curr]

                # Only teleport if the value itself is a prime number
                if val >= 2 and spf[val] == val:
                    
                    if val in buckets:
                        for nxt in buckets[val]:
                            if nxt not in visited:
                                visited.add(nxt)
                                queue.append(nxt)

                        # Kill switch optimization
                        del buckets[val]

            jumps += 1

        return -1