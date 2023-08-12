/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head){

    if(!head) return NULL;
    if(!head->next) return head;

    struct ListNode* even = head->next;
    struct ListNode* odd = head;
    struct ListNode* evenhead = head->next;

    while (odd->next && even->next){
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }

    odd->next = evenhead;

    return head;


    
}