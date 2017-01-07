/**
* Author: WuLC
* Date:   2017-01-07 11:14:29
* Last modified by:   WuLC
* Last Modified time: 2017-01-07 11:14:47
* Email: liangchaowu5@gmail.com
*/


// two demensional dp
public class Solution 
{
    public int uniquePaths(int m, int n) 
    {
        if (m==0 || n==0) return 0;
        int[][] dp = new int[m][n];
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if (i==0 || j==0) dp[i][j] = 1;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
}