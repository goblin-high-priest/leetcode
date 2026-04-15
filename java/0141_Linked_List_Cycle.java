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
// class Solution {
//     public boolean hasCycle(ListNode head) {
//         Set<ListNode> nodes = new HashSet<>();

//         while(head != null){

//             if(nodes.contains(head)){
//                 return true;
//             }

//             nodes.add(head);
//             head = head.next;

//         }

//         return false;
        
//     }
// }

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) return true;
        }

        return false;
        
    }
}