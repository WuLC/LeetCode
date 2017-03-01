/*
* @Author: WuLC
* @Date:   2017-03-01 08:43:58
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-01 08:51:10
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

// recursive method
public class Solution 
{
    public List<Integer> inorderTraversal(TreeNode root) 
    {
        List<Integer> curr = new ArrayList<Integer>();
        if (root == null) return curr;
        curr.add(root.val);
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        left.addAll(curr);
        left.addAll(right);
        return left;
    }
}



// stack, non-recursive
public class Solution 
{
    public List<Integer> inorderTraversal(TreeNode root) 
    {
        List<Integer> result = new ArrayList<Integer>();
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
                result.add(curr.val);
                curr = curr.right;
            }
        }
        return result;
    }
}
