/**
* Author: WuLC
* Date:   2017-02-14 13:51:49
* Last modified by:   WuLC
* Last Modified time: 2017-02-14 13:52:25
* Email: liangchaowu5@gmail.com
*/

// two dimentional dp, time O(n^2), space O(n^2)
// Java can AC , but Python get TLE

public class Solution 
{
    public int longestPalindromeSubseq(String s) 
    {
        int n = s.length();
        int[][] dp = new int[n][n];
        for(int i=n-1; i>=0; i--)
        {
            for(int j=i; j<n; j++)
            {
                if(i==j) dp[i][j] = 1;
                else if(s.charAt(i) == s.charAt(j)) dp[i][j] = dp[i+1][j-1] + 2;
                else dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
            }
        }
        return dp[0][n-1];
    }
}