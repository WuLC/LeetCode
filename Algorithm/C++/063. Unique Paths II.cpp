/*
 * Created on Fri May 04 2018 18:34:1
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// dp, O(m*n) space
class Solution 
{
    public:
        int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) 
        {
            if (obstacleGrid.size() == 0) return 0;
            int m = obstacleGrid.size(), n = obstacleGrid[0].size();
            int dp[m][n];
            for(int i=0; i<m; i++)
            {
                for(int j=0; j<n; j++)
                {
                    if (obstacleGrid[i][j] == 1) dp[i][j] = 0;
                    else
                    {
                        if (i==0 && j==0) dp[i][j] = 1;
                        else if(i==0) dp[i][j] = dp[i][j-1]==0 ? 0 : 1;
                        else if(j==0) dp[i][j] = dp[i-1][j]==0 ? 0 : 1;
                        else dp[i][j] = dp[i-1][j] + dp[i][j-1];   
                    }
                }
            }
            return dp[m-1][n-1];
    }
};