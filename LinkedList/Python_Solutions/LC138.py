class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        current = head
        while current:
            new = Node(current.val)
            new.next = current.next
            current.next = new
            current = new.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        current = head
        newhead = head.next
        while current:
            temp = current.next
            current.next  = temp.next
            if temp.next:
                temp.next = temp.next.next
            current = current.next        
        return newhead