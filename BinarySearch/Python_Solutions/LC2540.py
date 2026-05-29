# LC2540: Minimum  common values : https://leetcode.com/problems/minimum-common-value/

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Solve using Binary Search. Time complexity O(M log N)
        for i in nums1:
            # Binary search on nums1. 
            start1 =  0
            end1 = len(nums2) - 1
            while start1 < end1:
                m = start1 + (end1 - start1) // 2
                if i == nums2[m]:
                    return i
                if nums2[m] < i:
                    start1 = m + 1
                else:
                    end1 = m - 1
        # return - 1

        # Solve using two pointer. Time complexity O(M + N)
        l1, l2, r1, r2 = 0, 0, len(nums1), len(nums2)
        while l1 < r1 and l2 < r2:
            if nums1[l1] == nums2[l2]:
                return nums1[l1]

            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return -1