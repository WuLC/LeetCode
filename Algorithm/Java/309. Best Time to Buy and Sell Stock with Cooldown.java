/*
* @Author: WuLC
* @Date:   2017-03-16 21:05:45
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-16 21:07:00
* @Email: liangchaowu5@gmail.com
*/


// DP, O(n^2), dp[i] represents the max profit that selling stock on that day
// AC but slow
public class Solution 
{
    public int maxProfit(int[] prices) 
    {
        int n = prices.length;
        int[] dp = new int[n];
        int curr_max = 0;
        int result = 0;
        for(int i=0; i<n; i++)
        {
            for(int j=i; j>=0; j--)
            {
                if (j-2 >= 0) curr_max = Math.max(curr_max, Math.max(prices[i] - prices[j], 0) + dp[j-2]);
                else curr_max = Math.max(curr_max, prices[i] - prices[j]);
            }
            dp[i] = curr_max;
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}


//