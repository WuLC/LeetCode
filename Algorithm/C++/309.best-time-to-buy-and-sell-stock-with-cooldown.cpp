/*
 * @lc app=leetcode id=309 lang=cpp
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
#include <vector>



class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int len = prices.size();
        std::vector<std::vector<int>> dp(len, std::vector(4, 0));
        // two dimension dp
        // the first dimension is index of the day, the second is the states of the day(4 in total)
        // 0: hold the stock
        // 1: sell the stock on the i-th day(in cooldown)
        // 2: sell the stock last day(in cooldown)
        // 3: don't hold the stock(not in cooldown)
        dp[0][0] = -prices[0];
        for (int i = 1; i < len; i++) {
            dp[i][0] = std::max(dp[i-1][0], dp[i-1][3] - prices[i]);
            dp[i][1] = dp[i-1][0] + prices[i];
            dp[i][2] = dp[i][1];
            dp[i][3] = std::max(dp[i-1][3], dp[i-1][2]);
        }
        return std::max(std::max(dp[len-1][0], dp[len-1][1]), dp[len-1][3]);
    }
};
// @lc code=end

