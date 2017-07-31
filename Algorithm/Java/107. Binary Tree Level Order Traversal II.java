/*
* @Author: WuLC
* @Date:   2017-07-31 16:00:19
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-31 16:01:01
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

// traverse level by level
public class Solution 
{
    public List<List<Integer>> levelOrderBottom(TreeNode root) 
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null) return result;
        List<Integer> tmp;
        List<TreeNode> curr, next;
        next = new ArrayList<TreeNode>();
        next.add(root);
        while(next.size() > 0)
        {
            curr = next;
            next = new ArrayList<TreeNode>();
            tmp =  new ArrayList<Integer>();
            for(int i = 0; i < curr.size(); i++)
            {
                tmp.add(curr.get(i).val);
                if(curr.get(i).left != null)  next.add(curr.get(i).left);
                if(curr.get(i).right != null) next.add(curr.get(i).right);
            }  
            result.add(tmp);
        }
        Collections.reverse(result);
        return result;
    }
}