/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodes = new HashSet<>();

        while(head != null){

            if(nodes.contains(head)){
                return true;
            }

            nodes.add(head);
            head = head.next;

        }

        return false;
        
    }
}