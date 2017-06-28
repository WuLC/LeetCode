/*
* @Author: WuLC
* @Date:   2017-06-27 08:28:37
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-28 23:03:37
* @Email: liangchaowu5@gmail.com
*/

// dp
public class Solution 
{
    public int integerBreak(int n) 
    {
        int[] dp = new int[n+1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            int max = 0;
            for(int j = 1; j <= (i >> 1); j++)
            {
                max = Math.max( Math.max(dp[j], j) * Math.max(i - j, dp[i-j]), max);
            }
            dp[i] = max;
        }
        return dp[n];
    }
}

// dp with cache
public class Solution 
{
    private List<Integer> cache = new ArrayList<Integer>();
    public int integerBreak(int n) 
    {
        for (int i = cache.size(); i <= n; i++)
        {
            int max = 0;
            for(int j = 1; j <= (i >> 1); j++)
            {
                max = Math.max( Math.max(cache.get(j), j) * Math.max(i - j, cache.get(i-j)), max);
            }
            cache.add(max);
        }
        return cache.get(n);
    }
}