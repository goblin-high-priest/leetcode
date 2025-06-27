# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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

        while tail:

            if tail.val != head.val:
                return False

            head = head.next
            tail = tail.next
            
        return True