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
        if not head or not head.next or k == 0:
            return head
        # Solve in two phase.
        # First phase find the end of the list.
        # Assign the head to a value
        current = head
        n = 1
        while current.next is not None:
            current = current.next
            n += 1

        # Another case if the reminder is zero then after k number of rotation the value remain same.
        if k % n == 0:
            return head
        # calculate the break point.
        b = n - (k % n)

        # join the linkedlist for ring.
        current.next = head

        # Second pahse loop through the break point to find new head.
        new_node = head
        # Find the point where new head lies.
        for _ in range(b - 1):
            new_node = new_node.next
        # Record the new head.
        new_head = new_node.next
        # Make the current node the last node.
        new_node.next = None
        return new_head