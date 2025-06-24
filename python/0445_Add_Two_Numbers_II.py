# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(head):
            pre, cur = None, head

            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            return pre
        
        def addTwoLists(l1, l2):
            l3 = cur = ListNode(next=None)
            carry = 0

            while l1 or l2 or carry:
                val = carry
                val += l1.val if l1 else 0
                val += l2.val if l2 else 0
                carry = val // 10

                cur.next = ListNode(val % 10)
                
                if l1: l1 = l1.next 
                if l2: l2 = l2.next
                 
                cur = cur.next
            
            return l3
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        l3 = addTwoLists(l1, l2)

        return reverseList(l3.next)