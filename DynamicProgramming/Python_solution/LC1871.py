# LC1871: Jump Game VII : https://leetcode.com/problems/jump-game-vii/

from collections import defaultdict

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Calculate the length.
        n = len(s)
        # creating the linked list.
        reachable = defaultdict(set)
        # Loop through the array.
        for i in range(n):
            if s[i] == '1':
                continue
            # a. calculate the i + minjump.
            a = i + minJump
            # b. Calculate the min(i + maxjump, length).
            b = min(i + maxJump, n - 1)
            # loop through the a and b.
            for j in range(a, b + 1):
                # if the index value is 0.
                if s[j] == '0': 
                    # add to set.
                    reachable[i].add(j)
        for key, value_set in reachable.items():
            if (n - 1) in value_set:
                return True
        return False


from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
            
        n = len(s)
        queue = deque([0])
        
        farthest = 0
        
        while queue:
            curr = queue.popleft()
            
            if curr == n - 1:
                return True
                
            start = max(curr + minJump, farthest + 1)
            end = min(curr + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    queue.append(j)
                    
            farthest = max(farthest, end)
            
        return False
answer = Solution()
s = "011010"
minJump = 2
maxJump = 3
print(answer.canReach(s, minJump, maxJump))