# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)  # Dummy node for the "before x" list
        after_head = ListNode(0)   # Dummy node for the "after or equal x" list
        
        before = before_head
        after = after_head
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        # Combine the two lists
        after.next = None          # Important to avoid cycle
        before.next = after_head.next
        
        return before_head.next
