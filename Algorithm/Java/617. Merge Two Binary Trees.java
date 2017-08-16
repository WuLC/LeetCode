/*
* @Author: WuLC
* @Date:   2017-08-16 21:32:40
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-16 21:33:00
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

// recursive
public class Solution 
{
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) 
    {
        if(t1 == null && t2 == null) return null;
        else if(t1 == null) return t2;
        else if(t2 == null) return t1;
        TreeNode root = new TreeNode(0);
        root.val = t1.val + t2.val;
        root.left = mergeTrees(t1.left, t2.left);
        root.right = mergeTrees(t1.right, t2.right);
        return root;
    }
}