from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # No. 141
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next  
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next 
        return False