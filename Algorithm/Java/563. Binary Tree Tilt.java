/*
 * Created on Sat Feb 10 2018 14:51:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
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

 // bottom-up dfs
class Solution 
{
    private int result;
    public int findTilt(TreeNode root) 
    {
        result = 0;
        treeSum(root);
        return result;
    }
    
    public int treeSum(TreeNode root)
    {
        if (root == null) return 0;
        int leftSum = treeSum(root.left);
        int rightSum = treeSum(root.right);
        result += Math.abs(leftSum - rightSum);
        return leftSum+rightSum+root.val;
    }
}