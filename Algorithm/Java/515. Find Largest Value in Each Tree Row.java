/**
* Author: WuLC
* Date:   2017-04-29 10:54:10
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 10:54:31
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

// traverse the tree row by row
public class Solution 
{
    public List<Integer> largestValues(TreeNode root) 
    {
        if (root == null) return new ArrayList<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        List<TreeNode> curr, next;
        curr = new ArrayList<TreeNode>();
        curr.add(root);
        
        while(curr.size()>0)
        {
            int maxVal = Integer.MIN_VALUE;
            next = new ArrayList<TreeNode>();
            for(int i=0; i<curr.size(); i++)
            {
                TreeNode tmp = curr.get(i);
                if (tmp.left != null) next.add(tmp.left);
                if (tmp.right != null) next.add(tmp.right);
                maxVal = Math.max(maxVal, tmp.val);
            }
            result.add(maxVal);
            curr = next;
        }
        return result;
    }
}