/*
 * @lc app=leetcode id=322 lang=cpp
 *
 * [322] Coin Change
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        std::vector<int> dp(amount+1, -1);
        dp[0] = 0;
        for (int c : coins) {
            for (int i = c; i <= amount; i++) {
                if (dp[i-c] >= 0) {
                    if (dp[i] < 0) {
                        dp[i] = dp[i-c]+1;
                    } else {
                        dp[i] = std::min(dp[i], dp[i-c]+1);
                    }
                }
            }
        }
        return dp[amount];
    }
};
// @lc code=end

