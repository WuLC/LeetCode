/*
 * @lc app=leetcode id=516 lang=cpp
 *
 * [516] Longest Palindromic Subsequence
 */

// @lc code=start

#include <string>
#include <vector>

class Solution {
public:
    int longestPalindromeSubseq(std::string s) {
        int n = s.size();
        int result = 0;
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[i][j] = 1;
                } else if (s[i] == s[j]) {
                    dp[i][j] = 2;
                    if (i+1 <= j-1) {
                        dp[i][j] += dp[i+1][j-1];
                    }
                } else {
                    dp[i][j] = std::max(dp[i+1][j], dp[i][j-1]);
                    if (i+1 <= j-1) {
                        dp[i][j] = std::max(dp[i][j], dp[i+1][j-1]);
                    }
                }
                result = std::max(result, dp[i][j]);
            }
        }
        return result;
    }
};
// @lc code=end

