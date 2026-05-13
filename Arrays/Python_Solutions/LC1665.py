# LC1665: Minimum Initial Energy to Finish Task : https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        initial_energy = 0
        current_energy = 0
        for actual, minimum in tasks:
            if current_energy < minimum:
                deficit = minimum - current_energy
                initial_energy += deficit
                current_energy += deficit
            current_energy -= actual
        return initial_energy