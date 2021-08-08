/*
 * @lc app=leetcode id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
       int len = prices.size();
       std::vector<std::vector<int>> dp(len, std::vector<int>(2, 0));
       dp[0][0] = -prices[0];
       for (int i = 1; i < len; i++) {
           dp[i][0] = std::max(dp[i-1][0], dp[i-1][1] - prices[i]);
           dp[i][1] = std::max(dp[i-1][1], dp[i-1][0] + prices[i]);
       }
       return dp[len-1][1];        
    }
};
// @lc code=end

