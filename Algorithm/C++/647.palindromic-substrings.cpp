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
        int n = s.size(), result = 0;
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] && (i+1 >= j-1 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                    result += 1;
                }
            }
        }
        return result;
    }
};
// @lc code=end

