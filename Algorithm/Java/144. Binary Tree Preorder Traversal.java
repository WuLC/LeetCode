/*
* @Author: WuLC
* @Date:   2017-03-01 08:54:19
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-01 09:08:56
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
 
 // recusrive 
public class Solution 
{
    public List<Integer> preorderTraversal(TreeNode root) 
    {
        List<Integer> curr = new ArrayList<Integer>();
        if (root == null) return curr;
        curr.add(root.val);
        List<Integer> left = preorderTraversal(root.left);
        List<Integer> right = preorderTraversal(root.right);
        curr.addAll(left);
        curr.addAll(right);
        return curr;
    }
}

// use stack, non- recursive
public class Solution 
{
    public List<Integer> preorderTraversal(TreeNode root) 
    {
        List<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> nodes = new Stack<TreeNode>();
        TreeNode curr = root;
        while(nodes.size()>0 || curr!=null)
        {
            if (curr != null) 
            {
                result.add(curr.val);
                nodes.push(curr);
                curr = curr.left;
            }
            else
            {
                curr = nodes.pop();
                curr = curr.right;
            }
        }
        return result;
    }
}


