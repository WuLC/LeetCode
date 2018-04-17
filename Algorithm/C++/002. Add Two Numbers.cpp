/*
 * Created on Sun Apr 15 2018 10:23:9
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

 // addtion with carry
class Solution 
{
    public:
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
        {
            ListNode dummy(0), *p = &dummy;
            int carry = 0;
            while(l1 || l2 || carry)
            {
                if(l1)
                {
                    carry += l1->val;
                    l1 = l1->next;
                }
                if(l2)
                {
                    carry += l2->val;
                    l2 = l2->next;
                }
                p->next = new ListNode(carry%10);
                carry /= 10;
                p = p->next;
            }
            return dummy.next;
        }
};
