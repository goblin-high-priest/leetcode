# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = sentinel = ListNode(next=head)

        while cur.next and cur.next.next:

            if cur.next.val == cur.next.next.val:
                val = cur.next.val

                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        
        return sentinel.next