/*
 * Created on Fri May 04 2018 15:14:29
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, dp[i+1] represents the longest valid parentheses that ends with s[i]
class Solution 
{
    public:
        int longestValidParentheses(string s) 
        {
            int dp[s.size()+1] = {0};
            int result = 0;
            for(int i=0; i<s.size(); i++)
            {
                if (s[i] == '(') dp[i+1] = 0;
                else
                {
                    if (i-dp[i]-1>=0 && s[i-dp[i]-1]=='(')
                        dp[i+1] = 2 + dp[i] + dp[i-dp[i]-1];
                }
                result = std::max(result, dp[i+1]);
            }
            return result;
        }
};