/*
* @Author: WuLC
* @Date:   2017-06-20 10:26:55
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-20 12:22:52
* @Email: liangchaowu5@gmail.com
*/

// recursive with cache
public class Solution 
{
    private Map<Integer, Integer> cache = new HashMap<Integer, Integer>(); // TLE without cache
    public int numTrees(int n) 
    {
        if (cache.containsKey(n)) return cache.get(n);
        if (n <= 1) return n;
        int count = 0, left, right;
        for (int i = 0; i < n; i++)
        {
            left = numTrees(i);
            right = numTrees(n-i-1);
            if (left != 0 && right != 0) count += left * right;
            else count += left+right;
        }
        cache.put(n, count);
        return count;
    }
}


// dp without recursive
public class Solution 
{
    // dp[i] is the number of unique BST for i nodes
    private List<Integer> dp = new ArrayList<Integer>(); 
    public int numTrees(int n) 
    {
        if (dp.size() == 0) 
        {
            dp.add(0);
            dp.add(1);
        }
        for (int i = dp.size(); i <= n; i++)
        {
            int count = 0;
            for (int j = 0; j < i; j++) // number of nodes on the left sub tree
            {
                if ( j == 0 || j == i - 1) count += dp.get(i - 1);
                else count += dp.get(j) * dp.get(i-j-1);
            }
            dp.add(count);
        }
        return dp.get(n);
    }
}