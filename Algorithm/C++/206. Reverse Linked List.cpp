/*
 * Created on Wed Apr 18 2018 10:3:46
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

 // simple solution
class Solution 
{
    public:
        ListNode* reverseList(ListNode* head) 
        {
            if (head == NULL || head->next == NULL) return head;
            ListNode *pre = head;
            ListNode *curr = head->next;
            pre->next = NULL;
            while(curr != NULL)
            {
                ListNode *tmp = curr->next;
                curr->next = pre;
                pre = curr;
                curr = tmp;
            }
            return pre;
        }
};