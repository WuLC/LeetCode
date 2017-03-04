/*
* @Author: WuLC
* @Date:   2017-03-04 21:24:07
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-04 21:24:47
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



// find recursively
public class Solution 
{
    public int kthSmallest(TreeNode root, int k) 
    {
        int count = countNodes(root.left);
        if (count == k-1) return root.val;
        else if(count > k-1) return kthSmallest(root.left, k);
        else return kthSmallest(root.right, k-count-1);
    }
    
    public int countNodes(TreeNode root)
    {
        if (root == null) return 0;
        return 1+countNodes(root.left)+countNodes(root.right);
    }
}