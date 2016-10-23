/**
* Author: LC
* Date:   2016-10-23 08:53:44
* Last modified by:   WuLC
* Last Modified time: 2016-10-23 09:03:24
* Email: liangchaowu5@gmail.com
*/


//DP
//when '*' appears, discuss about the two cases when '*' represents nothing or any string
public class Solution 
{
    public boolean isMatch(String s, String p) 
    {
        int m = p.length()+1, n = s.length()+1;
        boolean[][] dp = new boolean[m][n];
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if(i==0)
                {
                    if(j==0) dp[i][j] = true;
                    else dp[i][j] = false;
                }
                else if(j==0)
                {
                    if(p.charAt(i-1)=='*') dp[i][j] = dp[i-1][j];
                    else dp[i][j] = false;
                }
                else
                {
                    if (p.charAt(i-1)=='?') dp[i][j] = dp[i-1][j-1];
                    else if(p.charAt(i-1)=='*') dp[i][j] = dp[i-1][j] || dp[i][j-1];
                    else dp[i][j] = (s.charAt(j-1)==p.charAt(i-1)) && dp[i-1][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
}