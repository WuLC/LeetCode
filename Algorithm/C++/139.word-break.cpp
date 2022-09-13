/*
 * @lc app=leetcode id=139 lang=cpp
 *
 * [139] Word Break
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::vector<bool> dp(s.size()+1, false);
        dp[0] = true;
        for (int i = 0; i <= s.size(); i++) {
            for (auto w : wordDict) {
                int n = w.size();
                if (i-n+1 >= 0 && dp[i-n+1] && s.substr(i-n+1, n) == w) {
                    dp[i+1] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};
// @lc code=end

