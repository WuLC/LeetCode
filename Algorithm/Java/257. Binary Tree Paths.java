/*
* @Author: WuLC
* @Date:   2017-07-02 17:01:24
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-02 17:01:48
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

// divide and conquer
public class Solution 
{
    public List<String> binaryTreePaths(TreeNode root) 
    {
        List<String> result = new ArrayList<String>();
        if(root == null) return result;
        String val = String.valueOf(root.val);
        if(root.left == null && root.right == null)
        {
            result.add(val);
            return result;
        }
        for(String s : binaryTreePaths(root.left)) result.add(val+"->"+s);
        for(String s : binaryTreePaths(root.right)) result.add(val+"->"+s);
        return result;
    }
}