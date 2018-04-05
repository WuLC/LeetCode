/*
 * Created on Thu Apr 05 2018 23:3:32
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp
// pay attention that we can not simply take dp[i] = dp[j] + dp[i-j], instead dp[i] = dp[i-j*j] + 1
class Solution 
{
    private ArrayList<Integer> dp = new ArrayList<Integer>(Arrays.asList(0));
    public int numSquares(int n) 
    {
        for (int i=dp.size(); i<=n; i++)
        {
            int curr = i;
            for(int j=1; j < (int)Math.sqrt(i)+1; j++)
            {
                curr = Math.min(curr, dp.get(i- j*j)+1);
            }
            dp.add(curr);
        }
        return dp.get(n); 
    }
}