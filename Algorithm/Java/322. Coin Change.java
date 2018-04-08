/**
* Author: LC
* Date:   2016-08-23 14:44:32
* Last modified by:   LC
* Last Modified time: 2016-08-23 15:06:21
* Email: liangchaowu5@gmail.com
*/


// DP with cache
class Solution 
{
    private ArrayList<Integer> dp = new ArrayList<Integer>(Arrays.asList(0));
    public int coinChange(int[] coins, int amount) 
    {
        Arrays.sort(coins);
        for(int i=dp.size(); i<=amount; i++)
        {
            int curr = -1;
            for(int coin:coins)
            {
                if (coin > i) break;
                if (dp.get(i-coin) == -1) continue;
                curr = curr==-1 ? dp.get(i-coin)+1: Math.min(curr, dp.get(i-coin)+1);
            }
            dp.add(curr);
        }
        return dp.get(amount);
    }
}


// DP, from top to bottom 
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