/**
* Author: WuLC
* Date:   2017-04-21 17:43:04
* Last modified by:   WuLC
* Last Modified time: 2017-04-21 19:43:17
* Email: liangchaowu5@gmail.com
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


// two recursive methods, the second one is a lot faster than the first one
// the reason is that the second method update the diameter at each node
public class Solution
{
    public int diameterOfBinaryTree(TreeNode root)
    {
        if (root == null) return 0;
        int maxLen = 0;
        if(root.left != null) maxLen += getMaxDepth(root.left)+1;
        if(root.right != null) maxLen += getMaxDepth(root.right)+1;
        int left = diameterOfBinaryTree(root.left);
        int right = diameterOfBinaryTree(root.right);
        return Math.max(Math.max(maxLen, left), right);
    }
    
    public int getMaxDepth(TreeNode root)
    {
        if (root == null || (root.left == null && root.right == null)) return 0;
        return Math.max(getMaxDepth(root.left), getMaxDepth(root.right)) + 1;
    }
}


public class Solution 
{
    private int diameter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) 
    {
        maxDepth(root);
        return diameter;
    }
    
    public int maxDepth(TreeNode root)
    {
        if (root == null) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        diameter = Math.max(diameter, left+right);
        return Math.max(left, right) + 1;
    }
}