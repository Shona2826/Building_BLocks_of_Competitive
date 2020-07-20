class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = prev = ListNode()
        ptr = head
        
        while ptr:
            if ptr.val != val:
                prev.next = ptr
                prev = prev.next
            
            ptr = ptr.next
        
        prev.next = None
        return root.next