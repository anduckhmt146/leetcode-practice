# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        # List A:     A1 → A2 → A3
        # List B: B1 → B2 → B3 → B4 → B5

        # ptrA path: A1 → A2 → A3 → B1 → B2 → B3 → B4 → B5 → None  
        # ptrB path: B1 → B2 → B3 → B4 → B5 → A1 → A2 → A3 → None
        while ptrA != ptrB:
            # Move each pointer to the next node, or switch lists at the end
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        # They either meet at the intersection or both become None (no intersection)
        return ptrA
