/**
* Author: WuLC
* Date:   2017-01-08 17:10:17
* Last modified by:   WuLC
* Last Modified time: 2017-01-08 17:10:42
* Email: liangchaowu5@gmail.com
*/

// two dimensional dp
public class Solution 
{
    public int minPathSum(int[][] grid) 
    {
        int m = grid.length, n = grid[0].length;
        if (m == 0 || n == 0) return 0;
        int[][] dp = new int[m][n];
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(i==0 && j==0) dp[i][j] = grid[i][j];
                else if(i==0) dp[i][j] = dp[i][j-1] + grid[i][j];
                else if(j==0) dp[i][j] = dp[i-1][j] + grid[i][j];
                else dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
}