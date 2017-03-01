/*
* @Author: WuLC
* @Date:   2017-03-01 08:58:26
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-01 09:08:49
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
    public List<Integer> postorderTraversal(TreeNode root) 
    {
        List<Integer> curr = new ArrayList<Integer>();
        if (root == null) return curr;
        curr.add(root.val);
        List<Integer> left = postorderTraversal(root.left);
        List<Integer> right = postorderTraversal(root.right);
        left.addAll(right);
        left.addAll(curr);
        return left;
    }
}


// use stack, non-recursive
// traverse  in the order mid-right-left, then reverse it
public class Solution 
{
    public List<Integer> postorderTraversal(TreeNode root) 
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
                curr = curr.right;
            }
            else
            {
                curr = nodes.pop();
                curr = curr.left;
            }
        }
        Collections.reverse(result);
        return result;   
        
    }
}