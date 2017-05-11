/**
* Author: WuLC
* Date:   2017-05-11 14:22:38
* Last modified by:   WuLC
* Last Modified time: 2017-05-11 14:29:05
* Email: liangchaowu5@gmail.com
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

// use hashmap to store the number of each sum 
// recursive to find all sum
public class Solution 
{
    private Map<Integer, Integer> count = new HashMap<Integer, Integer>();
    private int frequentCount = 0;
    public int[] findFrequentTreeSum(TreeNode root) 
    {
        List<Integer> record = new ArrayList<Integer>();
        if (root != null) dfs(root);
        for(Map.Entry<Integer, Integer> entry: count.entrySet())
            if (entry.getValue() == frequentCount)
                record.add(entry.getKey());
        int[] result = new int[record.size()];
        for(int i=0; i<record.size(); i++)  result[i] = record.get(i);
        return result;
    }
    
    public int dfs(TreeNode root)
    {
        if (root == null) return 0;
        int curr = root.val + dfs(root.left) + dfs(root.right);
        if (count.containsKey(curr)) count.put(curr, count.get(curr)+1);
        else count.put(curr, 1);
        frequentCount = Math.max(frequentCount, count.get(curr));
        return curr;
    }
}