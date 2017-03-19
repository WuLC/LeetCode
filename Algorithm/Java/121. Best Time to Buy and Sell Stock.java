/*
* @Author: WuLC
* @Date:   2017-03-17 19:42:43
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-17 19:43:45
* @Email: liangchaowu5@gmail.com
*/


// record the lowest price so far
public class Solution 
{
    public int maxProfit(int[] prices) 
    {
        if (prices.length == 0) return 0;
        int result = 0;
        int curr_min = prices[0];
        for(int i = 0; i < prices.length; i++)
        {
            result = Math.max(result, prices[i] - curr_min);
            curr_min = Math.min(curr_min, prices[i]);
        }
        return result;
    }
}