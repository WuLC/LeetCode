/*
 * Created on Sat Jun 02 2018 21:15:59
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

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 // recursive
class Solution 
{
    public:
        TreeNode* sortedListToBST(ListNode* head) 
        {
            vector<int> vals;
            while(head)
            {
                vals.push_back(head->val);
                head = head->next;
            }
            return helper(vals, 0, vals.size()-1);
        }
        
        TreeNode* helper(vector<int> vals, int s, int e)
        {
            if (s>e) return NULL;
            else if(s==e) return new TreeNode(vals[s]);
            else
            {
                int mid = s + ((e-s)>>1);
                TreeNode* root = new TreeNode(vals[mid]);
                root->left = helper(vals, s, mid-1);
                root->right = helper(vals, mid+1, e);
                return root;
            }
        }
    
    };