# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = p0 = ListNode(next=head)
        n = 0
        cur = head
        
        while cur:
            cur = cur.next
            n += 1
        
        pre, cur = None, head
        
        while n >= k:
            n -= k

            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        
        return sentinel.next