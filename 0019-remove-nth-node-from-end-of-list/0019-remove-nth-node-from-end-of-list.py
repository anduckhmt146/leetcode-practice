# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list. This helps simplify edge cases.
        dummy_node = ListNode(val=0, next=head)
      
        # Initialize two pointers to the dummy node.
        fast_pointer = slow_pointer = dummy_node
      
        # Move fast pointer n steps ahead so it maintains a gap of n between slow pointer.
        for _ in range(n):
            fast_pointer = fast_pointer.next
      
        # Move both pointers until fast pointer reaches the end of the list,
        # keeping the gap of n. Thus, the slow pointer will point to the node
        # just before the one to be removed.
        while fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next
      
        # Remove the nth node from the end by skipping over it with the slow pointer.
        slow_pointer.next = slow_pointer.next.next
      
        # Return the new head, which is the next node of dummy node.
        return dummy_node.next

        