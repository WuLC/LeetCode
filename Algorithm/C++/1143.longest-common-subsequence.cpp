/*
 * @lc app=leetcode id=1143 lang=cpp
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start

#include <vector>
#include <string>

class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        int m = text1.size(), n = text2.size(), result = 0;
        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i+1][j+1] = std::max(dp[i+1][j], dp[i][j+1]);
                if (text1[i] == text2[j]) {
                    dp[i+1][j+1] = std::max(dp[i][j]+1, dp[i+1][j+1]);
                }
                result = std::max(result, dp[i+1][j+1]);
            }
        }
        return result;
    }
};
// @lc code=end

