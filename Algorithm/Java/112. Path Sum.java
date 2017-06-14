/*
* @Author: WuLC
* @Date:   2017-06-14 14:12:51
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-14 14:13:07
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


// recursive
public class Solution 
{
    public boolean hasPathSum(TreeNode root, int sum) 
    {
        if (root == null) return false;
        if (root.left == null && root.right == null && root.val == sum) return true;
        else return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}