/*
* @Author: WuLC
* @Date:   2017-08-16 15:26:17
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-16 15:28:37
*/



// dp, time complexity: O(mn)
// dp[i+1][j+1] represents the number of distinct sequence given s[:i+1] and t[:j+1]
public class Solution 
{
    public int numDistinct(String s, String t) 
    {
        int sLen = s.length(), tLen = t.length();
        if(sLen < tLen) return 0;
        int[][] dp = new int[sLen + 1][tLen + 1];
        for(int i = 0; i < sLen; i++)
        {
            dp[i][0] = 1;
            for(int j = 0; j < tLen; j++)
            {
                if (s.charAt(i) == t.charAt(j)) dp[i+1][j+1] += dp[i][j];
                dp[i+1][j+1] += dp[i][j+1];
            }
        }
        return dp[sLen][tLen];
    }
}