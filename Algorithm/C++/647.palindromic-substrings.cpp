/*
 * @lc app=leetcode id=647 lang=cpp
 *
 * [647] Palindromic Substrings
 */

// @lc code=start

#include <string>
#include <vector>

class Solution {
public:
    int countSubstrings(std::string s) {
        int n = s.size();
        std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] && (i+1 >= j-1 || dp[i+1][j-1] == 1)) {
                    dp[i][j] = 1;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result += dp[i][j];
            }
        }
        return result;
    }
};
// @lc code=end

