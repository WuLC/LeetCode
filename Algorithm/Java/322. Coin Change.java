/**
* Author: LC
* Date:   2016-08-23 14:44:32
* Last modified by:   LC
* Last Modified time: 2016-08-23 15:06:21
* Email: liangchaowu5@gmail.com
*/


# DP, from bottom to top
public class Solution {
    public int coinChange(int[] coins, int amount) 
    {
        int[] dp = new int[amount+1];
        Arrays.fill(dp, amount+1);
        dp[0] = 0;
        for(int i=1;i<dp.length;i++)
        {
            for(int coin:coins)
            {
                if(i>=coin)
                    dp[i] = Math.min(dp[i], dp[i-coin]+1);
            }
        }
        if (dp[amount] == amount+1)
            return -1;
        else
            return dp[amount];
    }
}


# DP, from top to bottom 
public class Solution {
    Map<Integer, Integer> cache = new HashMap<Integer, Integer>();
    public int coinChange(int[] coins, int amount) 
    {
        if(amount==0)
            return 0;
        if(cache.containsKey(amount))
            return cache.get(amount);
        int tmp = amount+1;
        for(int coin:coins)
        {
            if(amount>=coin)
            {
                int next = coinChange(coins, amount-coin)+1;
                if(next>0)
                    tmp = Math.min(tmp, next);
            }
        }
        if(tmp == amount+1) 
            cache.put(amount, -1);
        else
            cache.put(amount, tmp);
        return cache.get(amount);
    }
}