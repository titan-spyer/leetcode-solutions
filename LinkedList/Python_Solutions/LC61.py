# LC61: Rotate List -> https://leetcode.com/problems/rotate-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base Case.
        if head is None:
            return None
        # Solve in two phase.
        # First phase find the end of the list.
        # Assign the head to a value
        current = head
        n = 1
        while current.next is not None:
            current = current.next
            n += 1

        # calculate the break point.
        b = n - (k % n)
        # join the linkedlist.
        current.next = head
        # Second pahse loop through the break point to find new head.
        new_node = head
        for i in range(b):
            new_node = new_node.next
        new_head = new_node.next
        new_node.next = None
        return new_head