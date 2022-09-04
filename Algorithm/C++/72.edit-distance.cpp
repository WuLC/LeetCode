/*
 * @lc app=leetcode id=72 lang=cpp
 *
 * [72] Edit Distance
 */

// @lc code=start

#include <string>
#include <vector>
#include <numeric>

class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int m = word1.size(), n = word2.size();

        // init dp matrix
        std::vector<std::vector<int>> dp(m+1, std::vector<int>(n+1, 0));
        for (int i = 0; i < m+1; i++) {
            for (int j = 0; j < n+1; j++)             
                if (i == 0) {
                    dp[i][j] = j;
                } else {
                    dp[i][0] = i;
                    break;
                }
        }

        // start iteration
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i+1][j+1] = std::min(dp[i][j],
                                std::min(dp[i+1][j], dp[i][j+1])) + 1;
                if (word1[i] == word2[j]) {
                    dp[i+1][j+1] = std::min(dp[i+1][j+1], dp[i][j]);
                }
            }
        }
        return dp[m][n];        
    }
};
// @lc code=end

