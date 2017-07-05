/*
* @Author: WuLC
* @Date:   2017-07-05 10:59:28
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-05 11:00:05
* @Email: liangchaowu5@gmail.com
*/


// dp
public class Solution 
{
    public int minDistance(String word1, String word2) 
    {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m+1][n+1];
        // init 
        for(int i = 0; i < m+1; i++) dp[i][0] = i;
        for(int j = 0; j < n+1; j++) dp[0][j] = j;
        
        // traverse
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(word1.charAt(i) == word2.charAt(j)) dp[i+1][j+1] = dp[i][j];
                else dp[i+1][j+1] = Math.min(dp[i][j+1], dp[i+1][j]) + 1;
            }
        }
        return dp[m][n];
    }
}