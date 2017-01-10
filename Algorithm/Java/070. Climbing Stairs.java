/**
* Author: WuLC
* Date:   2017-01-10 15:24:08
* Last modified by:   WuLC
* Last Modified time: 2017-01-10 15:24:41
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public int climbStairs(int n) 
    {
        int[] dp = new int[n];
        for(int i=0; i<n;i++) 
        {
            if (i==0) dp[i] = 1;
            else if(i==1) dp[i] = 2;
            else dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n-1];
    }
}