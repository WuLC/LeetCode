/*
* @Author: WuLC
* @Date:   2017-05-27 11:40:59
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-27 11:41:12
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

// recursive
public class Solution 
{
    public TreeNode sortedArrayToBST(int[] nums) 
    {
        return dfs(nums, 0, nums.length-1);
    }
    
    public TreeNode dfs(int[] nums, int start, int end)
    {
        if (start > end) return null;
        int mid = start + ((end - start) >> 1);
        TreeNode root = new TreeNode(nums[mid]);
        root.left = dfs(nums, start, mid - 1);
        root.right = dfs(nums, mid + 1, end);
        return root;
    }
}