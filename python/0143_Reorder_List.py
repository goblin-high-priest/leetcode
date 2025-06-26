# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def middleNode(head):
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverseList(head):
            pre, cur = None, head

            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            return pre

        tail = reverseList(middleNode(head))
        
        while tail.next:
            head_nxt = head.next
            tail_nxt = tail.next

            head.next = tail
            tail.next = head_nxt

            head = head_nxt
            tail = tail_nxt