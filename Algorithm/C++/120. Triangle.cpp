/*
 * Created on Tue May 08 2018 21:45:31
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// dp, O(n) space
class Solution 
{
    public:
        int minimumTotal(vector<vector<int>>& triangle) 
        {
            int m = triangle.size();
            int dp[m] = {0};
            for(int i=0; i<m; i++)
            {
                for(int j=i; j>=0; j--)
                {
                    if(j==0) dp[j] = triangle[i][j] + dp[j];
                    else if (j==i) dp[j] = triangle[i][j] + dp[j-1];
                    else dp[j] = triangle[i][j] + std::min(dp[j],dp[j-1]);
                }
            }
            int result = dp[0];
            for(int i=1; i<m; i++) result = std::min(result, dp[i]);
            return result;
        }
};