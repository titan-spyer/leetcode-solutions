from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        # Define Two dummy node.
        # Right Node.
        right_dummy = ListNode(0)
        # Left Node.
        left_dummy = ListNode(0)
        # Two tail. left and right
        left_tail = left_dummy
        right_tail = right_dummy
        curr = head
        # Loop through the list.
        while curr:
        # Add curr.val < x to left tail.
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
        # Add curr.val > x to right tail
            else:
                right_tail.next = curr
                right_tail = right_tail.next
        # Join them Together
            curr = curr.next
        right_tail.next = None
        left_tail.next = right_dummy.next
        return left_dummy.next