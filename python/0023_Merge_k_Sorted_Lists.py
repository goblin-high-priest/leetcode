# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None

        def merge(l1, l2):
            sentinel = ListNode()
            l3 = sentinel

            while l1 and l2:

                if l1.val < l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                
                l3 = l3.next
            
            if l1:
                l3.next = l1
            
            if l2:
                l3.next = l2

            return sentinel.next
        
        while len(lists) > 1:
            tmp_lists = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                l3 = merge(l1, l2)
                tmp_lists.append(l3)
            
            lists = tmp_lists
        
        return lists[0]
