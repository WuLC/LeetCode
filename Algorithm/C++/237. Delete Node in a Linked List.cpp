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
        void deleteNode(ListNode* node) 
        {
            while(true)
            {
                node->val = node->next->val;
                if (node->next->next == NULL)
                {
                    node->next = NULL;
                    return;
                }
                node = node->next;
            }
        }
};