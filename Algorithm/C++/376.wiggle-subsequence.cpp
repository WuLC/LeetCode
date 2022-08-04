/*
 * @lc app=leetcode id=376 lang=cpp
 *
 * [376] Wiggle Subsequence
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int wiggleMaxLength(std::vector<int>& nums) {
        int n = nums.size(), result = 0;
        std::vector<std::vector<int>> dp(2, std::vector<int>(n, 1));
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                for (int j = 0; j < i; j++) {
                    if (nums[j] < nums[i]) {
                        dp[0][i] = std::max(dp[1][j] + 1, dp[0][i]);
                    } else if (nums[j] > nums[i]) {
                        dp[1][i] = std::max(dp[0][j] + 1, dp[1][i]);
                    }
                }
            }
            result = std::max(result, dp[0][i]);
            result = std::max(result, dp[1][i]);
        }
        return result;
    }
};
// @lc code=end

