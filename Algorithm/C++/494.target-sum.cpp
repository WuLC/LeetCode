/*
 * @lc app=leetcode id=494 lang=cpp
 *
 * [494] Target Sum
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        // x - (sum - x) = target -> x = (sum+target)/2
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        int positive = (sum+target)>>1;
        if (((sum+target)&1) > 0 || positive < 0) {
            return 0;
        }
        std::vector<int> dp(positive+1, 0);
        dp[0] = 1;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = positive; j >= nums[i]; j--) {
                dp[j] += dp[j-nums[i]];
            }
        }
        return dp[positive];
    }
};
// @lc code=end

