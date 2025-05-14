# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Step 1: Initialize the heap with the head of each list
        for idx, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, idx, node))

        dummy = ListNode(0)
        current = dummy

        # Step 2: Extract min and add next node from the same list to the heap
        while heap:
            val, idx, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))

        return dummy.next
            