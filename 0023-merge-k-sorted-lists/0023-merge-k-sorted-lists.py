# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Assump we have 50 lists => change it multiple [list1, list2], [list3, list4]
        # Merge range
        # Merge 2 lists
        if not lists:
            return None
        return self.merge_range(lists, 0, len(lists) - 1)
        

    def merge_range(self, lists, left, right):
        # Base case
        # Mid
        # Merge 2 list

        if left == right:
            return lists[left]

        mid = (left + right) // 2

        l1 = self.merge_range(lists, left, mid)
        l2 = self.merge_range(lists, mid + 1, right)
        return self.merge_two_lists(l1, l2)
        

    def merge_two_lists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

