/**
* Author: WuLC
* Date:   2016-11-27 13:37:16
* Last modified by:   WuLC
* Last Modified time: 2016-11-27 13:38:58
* Email: liangchaowu5@gmail.com
*/

// DP
// dp[i] represents the longest valid parentheses that ends at s[i]

public class Solution 
{
    public int longestValidParentheses(String s) 
    {
        int[] dp = new int[s.length()+1];
        Arrays.fill(dp, 0);
        int result = 0;
        for (int i=1; i < s.length(); i++)
        {
            if (s.charAt(i) == '(') dp[i+1] = 0;
            else
            {
                if (s.charAt(i-1) == '(') dp[i+1] = dp[i-1]+2;
                else if ( i-1-dp[i] >= 0 && s.charAt(i-1-dp[i]) == '(') dp[i+1] = dp[i] + 2 + dp[i-1-dp[i]];
                else dp[i+1] = 0;
            }
            result = Math.max(result, dp[i+1]);
        }
        return result;
    }
}