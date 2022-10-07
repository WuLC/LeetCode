/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        std::string result = "";
        int n = s.size();
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) {
                    dp[i][j] = true;
                } else if (s[i] == s[j] && (i+1 >= j-1 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                }
                if (dp[i][j] && result.size() < j-i+1) {
                    result = s.substr(i, j-i+1);
                }
            }
        }
        return result;
    }
};
// @lc code=end

