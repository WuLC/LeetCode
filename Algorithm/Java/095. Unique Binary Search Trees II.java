/*
* @Author: WuLC
* @Date:   2017-06-20 19:55:20
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-20 19:55:32
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
    public List<TreeNode> generateTrees(int n) 
    {
        return helper(1, n);
    }
    
    public List<TreeNode> helper(int start, int end)
    {
        List<TreeNode> rootNodes = new ArrayList<TreeNode>();
        for(int i = start; i <= end; i++)
        {
            List<TreeNode> leftTrees = helper(start, i - 1);
            List<TreeNode> rightTrees = helper(i + 1, end);
            int leftCount, rightCount;
            if (leftTrees.size() == 0) leftTrees.add(null);
            if (rightTrees.size() == 0) rightTrees.add(null);
            for (int j = 0; j < leftTrees.size(); j++)
            {
                for(int k = 0; k < rightTrees.size(); k++)
                {
                    TreeNode root = new TreeNode(i);
                    root.left = leftTrees.get(j);
                    root.right = rightTrees.get(k);
                    rootNodes.add(root);
                }
            }
        }
        return rootNodes;
    }
}