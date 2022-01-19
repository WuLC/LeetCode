/*
 * @lc app=leetcode id=96 lang=cpp
 *
 * [96] Unique Binary Search Trees
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int numTrees(int n) {
        std::vector<int> dp(n+1, 0);
        dp[0] = 1, dp[1] = 1;
        for(int i=2; i<n+1; i++) {
            for(int j=0; j<i; j++) {
                dp[i] += dp[j]*dp[i-j-1];
            }
        }
        return dp[n];
    }
};
// @lc code=end
