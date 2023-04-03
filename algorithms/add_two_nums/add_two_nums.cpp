#include <iostream>

#include "../lib/list_node.h"

class Solution{
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            int carry = 0, sum;
            ListNode* ret = new ListNode();
            ListNode* head = ret;
            do
            {
                sum = carry;
                if (l1 != nullptr){
                    sum += l1->val;
                    l1 = l1->next;
                }

                if (l2 != nullptr){
                    sum += l2->val;
                    l2 = l2->next;
                }

                carry = sum / 10;
                sum = sum % 10;
                ret->val = sum;

                if ((l1 != nullptr) || (l2 != nullptr) || (carry != 0)){
                    ret->next = new ListNode();
                }
                ret = ret->next;

                if ((l1 == nullptr) && (l2 == nullptr) && (carry != 0)){
                    ret->val = carry;
                }

            } while ((l1 != nullptr) || (l2 != nullptr));

            return head;

        }
};

int main(int argc, char const *argv[])
{
    ListNode* in1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode* in2 = new ListNode(5, new ListNode(6, new ListNode(4)));

    Solution s = Solution();
    ListNode* ans = s.addTwoNumbers(in1, in2);
    while (ans != nullptr){
        std::cout << ans->val << " ";
        ans = ans->next;
    }
    std::cout << std::endl;

    return 0;
}
