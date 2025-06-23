# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        node1 = head
        node2 = head.next
        node3 = head.next.next

        node2.next = node1
        node1.next = self.swapPairs(node3)

        return node2