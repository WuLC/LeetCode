/**
* Author: WuLC
* Date:   2017-04-29 10:39:40
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 10:40:02
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

// recursive 
public class Solution 
{
    public boolean isSameTree(TreeNode p, TreeNode q) 
    {
        if (p == null && q == null) return true;
        else if(p==null || q == null) return false;
        else return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}