# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node is already sorted
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves using fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Cut the list into two parts

        # Step 2: Sort each half recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Append the remaining part
        tail.next = l1 or l2
        
        return dummy.next
