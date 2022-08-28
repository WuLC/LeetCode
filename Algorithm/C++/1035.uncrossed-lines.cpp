/*
 * @lc app=leetcode id=1035 lang=cpp
 *
 * [1035] Uncrossed Lines
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int maxUncrossedLines(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), result = 0;
        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i+1][j+1] = std::max(dp[i+1][j], dp[i][j+1]);
                if (nums1[i] == nums2[j]) {
                    dp[i+1][j+1] = std::max(dp[i][j]+1, dp[i+1][j+1]);
                }
                result = std::max(result, dp[i+1][j+1]);
            }
        }
        return result;
    }
};
// @lc code=end

