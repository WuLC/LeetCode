/*
* @Author: WuLC
* @Date:   2017-06-28 09:21:15
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-28 09:21:40
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


// traverse level by level with flag
public class Solution 
{
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) 
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) return result;
        List<TreeNode> curr = new ArrayList<TreeNode>();
        curr.add(root);
        boolean fromLeft = true;
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
            if (fromLeft == true) fromLeft = false;
            else
            {
                Collections.reverse(nums);
                fromLeft = true;
            }
            result.add(nums);
        }
        return result;        
    }
}