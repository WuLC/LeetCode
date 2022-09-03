/*
 * @lc app=leetcode id=583 lang=cpp
 *
 * [583] Delete Operation for Two Strings
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int m = word1.size(), n = word2.size();
        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i+1][j+1] = std::max(dp[i][j+1], dp[i+1][j]);
                if (word1[i] == word2[j]) {
                    dp[i+1][j+1] = std::max(dp[i][j]+1, dp[i+1][j+1]);
                }
            }
        }
        return m + n - 2*dp[m][n];
    }
};
// @lc code=end

