/*
 * @lc app=leetcode id=377 lang=cpp
 *
 * [377] Combination Sum IV
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) {
        std::vector<uint64_t> dp(target+1, 0);
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i >= num) {
                    dp[i] += dp[i-num];
                }
            }
        }
        return dp[target];
    }
};
// @lc code=end

