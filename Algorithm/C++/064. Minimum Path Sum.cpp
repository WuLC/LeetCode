/*
 * Created on Sun May 06 2018 9:9:5
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, O(n) space
class Solution 
{
    public:
        int minPathSum(vector<vector<int>>& grid) 
        {
            if(grid.size() == 0) return 0;
            int m=grid.size(), n=grid[0].size();
            int dp[n+1] = {0};
            for(int i=0; i<m; i++)
            {
                for(int j=0; j<n; j++)
                {
                    if(i==0) dp[j+1] = dp[j] + grid[i][j];
                    else if(j==0) dp[j+1] = dp[j+1] + grid[i][j];
                    else dp[j+1] = std::min(dp[j], dp[j+1]) + grid[i][j]; 
                }
            }
            return dp[n];
        }
};