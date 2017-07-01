/*
* @Author: WuLC
* @Date:   2017-07-01 16:43:14
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-01 16:43:29
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

// traverse the tree level by level
public class Solution 
{
    public int findBottomLeftValue(TreeNode root) 
    {
        List<TreeNode> curr = new ArrayList<TreeNode>();
        curr.add(root);
        int result = 0;
        while(curr.size() > 0)
        {
            result = curr.get(0).val;
            List<TreeNode> next = new ArrayList<TreeNode>();
            for(TreeNode node : curr)
            {
                if (node.left != null) next.add(node.left);
                if (node.right != null) next.add(node.right);
            }
            curr = next;
        }
        return result;
    }
}