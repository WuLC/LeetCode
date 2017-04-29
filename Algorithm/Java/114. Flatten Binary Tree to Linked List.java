/**
* Author: LC
* Date:   2017-04-29 09:56:45
* Last modified by:   WuLC
* Last Modified time: 2017-04-29 10:00:53
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


// recursive, combine flattened left-subtree and flattened righ-subtree each time 
public class Solution
{
    public void flatten(TreeNode root) 
    {
        helper(root);
    }
    
    public TreeNode[] helper(TreeNode root)  // return the head and tail of a tree after being flattened
    {
        TreeNode[] nodes = new TreeNode[2];
        Arrays.fill(nodes, null);
        if (root != null)
        {
            nodes[0] = root;
            if (root.left == null && root.right == null)
            {
                nodes[1] = root;
            }
            else
            {
                TreeNode[] leftNodes = helper(root.left);
                TreeNode[] rightNodes = helper(root.right);
                root.left = null;
                if (leftNodes[0] != null) 
                {
                    root.right = leftNodes[0];
                    if (rightNodes[0] == null) nodes[1] = leftNodes[1];
                    else
                    {
                        leftNodes[1].right = rightNodes[0];
                        nodes[1] = rightNodes[1];
                    }
                }
                else  
                {
                    root.right = rightNodes[0];
                    nodes[1] = rightNodes[1];
                }
            }
        }
        return nodes;
    }
}