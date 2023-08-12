/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    if(!head) return NULL;
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    struct ListNode* next = head->next;

    while (curr){
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}