/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include "../lib/list_node.h"

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode *current = head, *temp;
        while (current != nullptr){
            count++;
            current = current->next;
        }
        if (count == n) return head->next;
        current = head;
        temp = current;
        // count until
        while (count > n){
            count--;
            temp = current;
            current = current->next;
        }
        temp->next = current->next;
        current->next = nullptr;
        return head;
    }
};

// I don't want to build the Linked List now
