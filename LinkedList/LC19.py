# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a singly linked list and returns its head.
        
        This solution uses a two-pointer (fast and slow) approach to find the target 
        node in a single pass. A dummy node is used to elegantly handle edge cases, 
        such as when the head of the list itself needs to be removed.
        
        Args:
            head (Optional[ListNode]): The head of the singly linked list.
            n (int): The position from the end of the list of the node to remove.
            
        Returns:
            Optional[ListNode]: The head of the modified linked list.
            
        Complexity:
            Time: O(L), where L is the number of nodes in the list. Only one pass is made.
            Space: O(1), as only constant extra space is used for the pointers.
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next