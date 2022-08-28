/*
 * @lc app=leetcode id=300 lang=cpp
 *
 * [300] Longest Increasing Subsequence
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        int result = 1;
        std::vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++) {
            for (int j = i-1; j >= 0; j--) {
                if (nums[i] > nums[j]) {
                    dp[i] = std::max(dp[i], dp[j] + 1);
                }
            }
            result = std::max(result, dp[i]);
        }
        return result;
    }
};
// @lc code=end

