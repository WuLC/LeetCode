/*
* @Author: WuLC
* @Date:   2017-03-01 09:15:43
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-01 09:16:20
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


// inorder traverse and judge whether the values array is ascending
public class Solution 
{
    public boolean isValidBST(TreeNode root) 
    {
        List<Integer> values = new ArrayList<Integer>();
        Stack<TreeNode> nodes = new Stack<TreeNode>();
        TreeNode curr = root;
        while(nodes.size()>0 || curr!=null)
        {
            if (curr != null) 
            {
                nodes.push(curr);
                curr = curr.left;
            }
            else
            {
                curr = nodes.pop();
                values.add(curr.val);
                curr = curr.right;
            }
        }
        // judge whether arraylist is ascending
        for(int i=1; i < values.size(); i++)
        {
            if (values.get(i) <= values.get(i-1))
                return false;
        }
        return true;
    }
}