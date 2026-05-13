# LC1674: Minimum moves to make array complementary : https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        # 1. Initialize the Difference Array
        # Size needs to be (2 * limit + 2) to safely handle the "+ 1" edge cases
        diff = [0] * (2 * limit + 2)
        
        # 2. Process Every Pair (The Discount System)
        for i in range(n // 2):
            
            # Identify the smaller and larger number in the pair
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])
            
            # Apply the 4 Decision Rules to our timeline
            # Rule 1: Enter the 1-move window
            diff[A + 1] -= 1
            
            # Rule 2: Hit the exact 0-move target
            diff[A + B] -= 1
            
            # Rule 3: Leave the exact 0-move target (back to 1 move)
            diff[A + B + 1] += 1
            
            # Rule 4: Leave the 1-move window (back to 2 moves)
            diff[B + limit + 1] += 1

        # 3. Sweep the Array to Find the Minimum Cost
        # Baseline cost: assume every pair takes 2 moves
        current_moves = n  
        min_moves = n
        
        # We only care about target sums from 2 up to 2 * limit
        for target in range(2, (2 * limit) + 1):
            
            # Add the current timeline's discount/penalty to our running total
            current_moves += diff[target]
            
            # Update our all-time best record
            min_moves = min(min_moves, current_moves)
            
        return min_moves