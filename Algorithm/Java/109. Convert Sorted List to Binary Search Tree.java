/*
* @Author: WuLC
* @Date:   2017-05-27 11:21:08
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-27 11:21:26
* @Email: liangchaowu5@gmail.com
*/


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// recursive, O(n) space
public class Solution 
{
    public TreeNode sortedListToBST(ListNode head) 
    {
        List<Integer> vals = new ArrayList<Integer>();
        ListNode curr = head;
        while(curr != null)
        {
            vals.add(curr.val);
            curr = curr.next;
        }
        return dfs(vals, 0, vals.size()-1);
    }
    
    public TreeNode dfs(List<Integer> vals, int start, int end)
    {
        if (start > end) return null;
        int mid = start + ((end - start)>>1);
        TreeNode root = new TreeNode(vals.get(mid));
        root.left = dfs(vals, start, mid-1);
        root.right = dfs(vals, mid + 1, end);
        return root;
    }
}