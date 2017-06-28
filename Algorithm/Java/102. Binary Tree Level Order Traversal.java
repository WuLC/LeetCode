/*
* @Author: WuLC
* @Date:   2017-06-28 08:50:42
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-28 08:50:55
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
    public List<List<Integer>> levelOrder(TreeNode root) 
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) return result;
        List<TreeNode> curr = new ArrayList<TreeNode>();
        curr.add(root);
        while(curr.size() != 0)
        {
            List<TreeNode> next = new ArrayList<TreeNode>();
            List<Integer> nums = new ArrayList<Integer>();
            TreeNode tmp;
            for (int i = 0; i < curr.size(); i++)
            {
                tmp = curr.get(i);
                nums.add(tmp.val);
                if(tmp.left != null) next.add(tmp.left);
                if(tmp.right != null) next.add(tmp.right);
            }
            curr = next;
            result.add(nums);
        }
        return result;
    }
}