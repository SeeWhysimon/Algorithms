from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # No. 61
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        old_tail, length = head, 1
        while old_tail.next:
            length += 1
            old_tail = old_tail.next
        k = k % length
        if k == 0:
            return head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = head
        return new_head

    # No. 106 ***
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        ptr1, ptr2 = headA, headB
        while ptr1 != ptr2:
            ptr1 = ptr1 if ptr1 else headB
            ptr2 = ptr2 if ptr2 else headA
        return ptr1

    # No. 141
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next 
        return False
    
    # No. 142 ***
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    # No. 147
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # My version O(n^2)
        ''' 
            if not head or not head.next:
                return head
            fast = head.next
            while fast:
                slow = head
                while slow != fast:
                    if slow.val > fast.val:
                        slow.val, fast.val = fast.val, slow.val
                        break
                    slow = slow.next
                fast = fast.next
            return head
        '''  
        # Official version O(n) ~ O(n^2)
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
                continue
            to_insert = curr.next
            curr.next = curr.next.next
            prev = dummy
            while prev.next.val < to_insert.val:
                prev = prev.next
            to_insert.next = prev.next
            prev.next = to_insert
        return dummy.next 
    
    # No.237
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
