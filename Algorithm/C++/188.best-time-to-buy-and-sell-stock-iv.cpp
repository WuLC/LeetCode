/*
 * @lc app=leetcode id=188 lang=cpp
 *
 * [188] Best Time to Buy and Sell Stock IV
 */

// @lc code=start

#include<vector>

class Solution {
public:
    int maxProfit(int k, std::vector<int>& prices) {
        int len = prices.size(), result = 0;
        if (len == 0) return result;
        std::vector<std::vector<int>> dp(len, std::vector<int>(2*k+1, 0));
        for (int j = 1; j <= k; j++) {
            dp[0][2*j-1] = -prices[0];
        }
        for (int i=1; i < len; i++) {
            for (int j=1; j <= k; j++) {
                int buy = 2*j-1, sell = 2*j;
                dp[i][buy] = std::max(dp[i-1][buy], dp[i][buy-1] - prices[i]);
                dp[i][sell] = std::max(dp[i-1][sell], dp[i][sell-1] + prices[i]);
                result = std::max(result, dp[i][sell]);
            }
        }
        return result;
        
    }
};
// @lc code=end

