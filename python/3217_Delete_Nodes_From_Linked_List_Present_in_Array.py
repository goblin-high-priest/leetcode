# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        cur = sentinel = ListNode(next=head)

        while cur.next:
            
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return sentinel.next