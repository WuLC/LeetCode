/*
* @Author: WuLC
* @Date:   2017-08-07 12:45:47
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-07 12:46:31
* @Email: liangchaowu5@gmail.com
*/


// top-bottom dp
// referer: https://discuss.leetcode.com/topic/51353/simple-dp-solution-with-explanation
public class Solution 
{
    private int[][] dp;
    public int getMoneyAmount(int n) 
    {
        dp = new int[n + 1][n + 1];
        return helper(1, n);
    }
    
    public int helper(int s, int e)
    {
        if(s >= e) return 0;
        if (dp[s][e] == 0)
        {
            int tmp = Integer.MAX_VALUE;
            for(int i = s; i <= e; i++) tmp = Math.min(tmp, i + Math.max(helper(s, i - 1), helper(i + 1, e)));
            dp[s][e] = tmp;
        }
        return dp[s][e];
    }
}