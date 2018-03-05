/*
 * Created on Sun Feb 11 2018 15:49:33
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

 // recursive
class Solution 
{
    public boolean isSubtree(TreeNode s, TreeNode t) 
    {
        if (t == null) 
            return true;
        else if(s == null) 
            return false;
        else
            return sameTree(s, t) || isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean sameTree(TreeNode t1, TreeNode t2)
    {
        if (t1==null && t2 == null)
            return true;
        else if (t1==null || t2==null)
            return false;
        else
            return t1.val==t2.val && sameTree(t1.left, t2.left) && sameTree(t1.right, t2.right);
    }
}