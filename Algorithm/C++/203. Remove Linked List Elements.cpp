/*
 * Created on Tue May 22 2018 20:25:11
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

 // simple solution, two pointers
class Solution 
{
    public:
        ListNode* removeElements(ListNode* head, int val) 
        {
            ListNode* dummy = new ListNode(0);
            ListNode* p1=dummy;
            if (dummy) dummy->next = head;
            while(head)
            {
                if(head->val != val && p1!= NULL)
                {
                    p1->next = head;
                    p1 = p1->next;
                }
                head = head->next;
            }
            if (p1) p1->next = NULL;
            if (dummy) return dummy->next;
            else return NULL;
        }
};