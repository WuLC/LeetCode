/*
 * @lc app=leetcode id=132 lang=cpp
 *
 * [132] Palindrome Partitioning II
 */

// @lc code=start

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int minCut(std::string s) {
        int n = s.size();
        std::vector<std::vector<bool>> is_palidorme(n, std::vector<bool>(n, false));
        for (int i = n-1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] && (i+1 >= j-1 || is_palidorme[i+1][j-1])) {
                    is_palidorme[i][j] = true;
                }
            }
        }
        
        std::vector<int> dp(n, INT_MAX);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (is_palidorme[j][i]) {
                    if (j == 0) {
                        dp[i] = 0;
                    } else {
                        dp[i] = std::min(dp[i], dp[j-1]+1);
                    }
                }
            }
        }
        return dp[n-1];
    }
};
// @lc code=end

