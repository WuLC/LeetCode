/*
 * @lc app=leetcode id=343 lang=cpp
 *
 * [343] Integer Break
 */

// @lc code=start

#include <vector>

class Solution {
public:
    int integerBreak(int n) {
        std::vector<int> dp(n+1, 0);
        dp[1] = 1;
        for (int i=2; i <= n; i++) {
            for (int j=1; j <= i-1; j++) {
                dp[i] = std::max(dp[i], std::max(j * (i-j), j*dp[i-j]));
            }
        }
        return dp[n];
    }
};
// @lc code=end

