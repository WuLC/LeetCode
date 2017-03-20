/**
* Author: WuLC
* Date:   2017-03-20 23:20:36
* Last modified by:   WuLC
* Last Modified time: 2017-03-20 23:22:45
* Email: liangchaowu5@gmail.com
*/

// dp, O(n^2)
// dp[i] represents whether s[:i] can be segmented  
public class Solution 
{
    public boolean wordBreak(String s, List<String> wordDict) 
    {
        Set<String> words = new HashSet<String>();
        boolean[] dp = new boolean[s.length()+1];
        Arrays.fill(dp, false);
        dp[0] = true;
        for(String word : wordDict)
            words.add(word);
        for(int i = 0; i < s.length(); i++)
        {
            for(int j = 0; j <= i; j++)
            {
                if(dp[j] && words.contains(s.substring(j,i+1)))
                {
                    dp[i+1] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}