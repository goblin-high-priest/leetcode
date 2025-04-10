/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 struct ListNode* createNode(int value) {
    struct ListNode* newNode = (struct ListNode*) malloc(sizeof(struct ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* headNode = createNode(0);
    struct ListNode* linkedList = headNode;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int digit1 = (l1 != NULL) ? l1->val : 0;
        int digit2 = (l2 != NULL) ? l2->val : 0;

        int sum = digit1 + digit2 + carry;
        int digit = sum % 10;
        carry = sum / 10;

        struct ListNode* node = createNode(digit);
        linkedList->next = node;
        linkedList = linkedList->next;

        l1 = (l1 != NULL) ? l1->next : NULL;
        l2 = (l2 != NULL) ? l2->next : NULL;
    }
    return headNode->next;
}