/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        std::vector<int> dp(nums.size());
        int result = nums[0];
        dp[0] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = std::max(nums[i], dp[i-1] + nums[i]);
            result = std::max(dp[i], result);
        }
        return result;
    }
};
// @lc code=end

