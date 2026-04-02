# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second =  slow.next
        slow.next = None
        prev = None
        while second:
            second.next, prev, second = prev, second, second.next
        a = head
        b = prev
        while b:
            tempa, tempb = a.next, b.next
            a.next, b.next = b, tempa
            a, b = tempa, tempb

        
        