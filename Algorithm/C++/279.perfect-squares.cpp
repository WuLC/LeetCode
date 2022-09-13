/*
 * @lc app=leetcode id=279 lang=cpp
 *
 * [279] Perfect Squares
 */

// @lc code=start

#include <vector>
#include <cmath>

class Solution {
public:
    int numSquares(int n) {
        std::vector<int> dp(n+1, 0);
        for (int i = 0; i <= n; i++) {
            dp[i] = i;
        }
        for (int i = 1; i <= int(sqrt(n)); i++) {
            for (int j = i*i; j <= n; j++) {
                dp[j] = std::min(dp[j], dp[j - i*i] + 1);
            }
        }
        return dp[n];
    }
};
// @lc code=end

