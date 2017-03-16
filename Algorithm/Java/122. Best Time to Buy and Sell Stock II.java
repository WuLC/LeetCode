/*
* @Author: WuLC
* @Date:   2017-03-16 20:34:06
* @Last Modified by:   WuLC
* @Last Modified time: 2017-03-16 20:35:18
* @Email: liangchaowu5@gmail.com
*/


// greedy, sell when current price is higher than previous price and buy when currrnt price is lower than current price
public class Solution 
{
    public int maxProfit(int[] prices)
    {
        if (prices.length == 0) return 0;
        int profit = 0;
        int curr_price = prices[0];
        for (int i = 1; i < prices.length; i++)
        {
            if (prices[i] > curr_price) 
            {
                profit += prices[i] - curr_price;
                curr_price = prices[i];
            }
            else  curr_price = prices[i];
        }
        return profit;
    }
}