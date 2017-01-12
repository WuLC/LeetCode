/**
* Author: WuLC
* Date:   2017-01-12 11:33:03
* Last modified by:   WuLC
* Last Modified time: 2017-01-12 11:33:30
* Email: liangchaowu5@gmail.com
*/


// two dimensional dp
public class Solution 
{
    public int minDistance(String word1, String word2) 
    {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m+1][n+1];
        for(int i=0; i<m+1; i++)
        {
            for(int j=0; j<n+1; j++)
            {
                if(i == 0) dp[i][j] = j;
                else if(j == 0) dp[i][j] = i;
                else if (word1.charAt(i-1) == word2.charAt(j-1)) dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]) + 1, dp[i-1][j-1]);
                else dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
            }
        }
        return dp[m][n];
    }
}