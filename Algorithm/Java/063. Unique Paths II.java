/**
* Author: WuLC
* Date:   2017-01-07 11:25:54
* Last modified by:   WuLC
* Last Modified time: 2017-01-07 11:27:06
* Email: liangchaowu5@gmail.com
*/

// two dimensional dynamic programming
public class Solution 
{
    public int uniquePathsWithObstacles(int[][] obstacleGrid) 
    {
        if(obstacleGrid.length == 0) return 0;
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(obstacleGrid[i][j] == 1) dp[i][j] = 0;
                else if(i == 0)
                {
                    if(j==0) dp[i][j] = 1;
                    else dp[i][j] = dp[i][j-1];
                }
                else if(j==0) dp[i][j] = dp[i-1][j];
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
}