/*
* @Author: WuLC
* @Date:   2017-03-01 09:25:34
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-01 09:26:28
* @Email: liangchaowu5@gmail.com
*/

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */



// traverse the tree in the order right-mid-left and store them in a tree 
public class BSTIterator 
{
    private Stack<Integer> values;
    public BSTIterator(TreeNode root) 
    {
        values = new Stack<Integer>();
        Stack<TreeNode> nodes = new Stack<TreeNode>();
        TreeNode curr = root;
        while(nodes.size()>0 || curr!=null)
        {
            if (curr != null) 
            {
                nodes.push(curr);
                curr = curr.right;
            }
            else
            {
                curr = nodes.pop();
                values.push(curr.val);
                curr = curr.left;
            }
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() 
    {
        return values.size() != 0;
    }

    /** @return the next smallest number */
    public int next() 
    {
        return values.pop();
    }
}