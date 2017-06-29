/*
* @Author: WuLC
* @Date:   2017-06-29 14:54:40
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-29 14:55:09
* @Email: liangchaowu5@gmail.com
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

// divide and conquer
public class Solution 
{
    public int rob(TreeNode root) 
    {
        if(root == null) return 0;
        int tmp = root.val;
        if(root.left != null) tmp += rob(root.left.left) + rob(root.left.right);
        if(root.right != null) tmp += rob(root.right.left) + rob(root.right.right);
        return Math.max(tmp, rob(root.left) + rob(root.right));
    }
}