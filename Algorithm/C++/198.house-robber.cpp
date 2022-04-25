/*
 * @lc app=leetcode id=198 lang=cpp
 *
 * [198] House Robber
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        std::vector<int> dp(nums.size() + 1, 0);
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) {
                dp[i+1] = nums[i];
            } else {
                dp[i+1] = std::max(dp[i], dp[i-1] + nums[i]);
            }
        }
        return dp[nums.size()];
    }
};
// @lc code=end

