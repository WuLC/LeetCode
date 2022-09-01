/*
 * @lc app=leetcode id=115 lang=cpp
 *
 * [115] Distinct Subsequences
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    int numDistinct(std::string s, std::string t) {
        int m = s.size(), n = t.size();
        std::vector<std::vector<uint64_t>> dp(m+1, std::vector<uint64_t>(n+1, 0));
        for (int i = 0; i < m+1; i++) {
            dp[i][0] = 1;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j > i) continue;
                dp[i+1][j+1] = std::max(dp[i+1][j+1], dp[i][j+1]);
                if (s[i] == t[j]) {
                    dp[i+1][j+1] = std::max(dp[i+1][j+1], dp[i][j] + dp[i][j+1]);
                }
            }
        }
        return dp[m][n];
    }
};
// @lc code=end

