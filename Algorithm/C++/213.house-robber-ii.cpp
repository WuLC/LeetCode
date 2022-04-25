/*
 * @lc app=leetcode id=213 lang=cpp
 *
 * [213] House Robber II
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        } else if (nums.size() == 1) {
            return nums[0];
        } else {
            return std::max(helper(nums, 0, nums.size()-2),
                            helper(nums, 1, nums.size()-1));
        }
    }

private:
    int helper(std::vector<int>& nums, int start, int end) {
        std::vector<int> dp(end - start + 2, 0);
        for (int i=start; i <= end; i++) {
           if (i == start) {
               dp[i - start + 1] = nums[i];
           } else {
               dp[i - start + 1] = std::max(dp[i - start], dp[i-start-1] + nums[i]);
           }
        }
        return dp[end - start + 1];
    }
};
// @lc code=end

