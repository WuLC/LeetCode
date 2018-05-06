/*
 * Created on Sun May 06 2018 9:45:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, the solution can deal with different cost for insert, replace and remove 
// in this problem convert word1 to word2 is equal to converting word2 to word1
class Solution 
{
    public:
        int minDistance(string word1, string word2) 
        {
            int m = word1.length(), n = word2.length();
            int dp[m+1][n+1];
            int insert = 1, replace = 1, remove = 1;
            for(int i=0; i<m+1; i++)
            {
                for(int j=0; j<n+1; j++)
                {
                    if(i==0 && j==0) dp[i][j] = 0;
                    else if(i==0) dp[i][j] = dp[i][j-1] + remove; 
                    else if(j==0) dp[i][j] = dp[i-1][j] + insert;
                    else
                    {
                        if (word1[i-1] == word2[j-1]) dp[i][j] = dp[i-1][j-1];
                        else dp[i][j] = std::min(std::min(dp[i-1][j-1]+replace ,dp[i-1][j]+insert), dp[i][j-1]+remove);
                    }
                }
            }
            return dp[m][n];
        }
};