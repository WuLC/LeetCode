/*
 * @lc app=leetcode id=416 lang=cpp
 *
 * [416] Partition Equal Subset Sum
 */

// @lc code=start
#include <vector>
#include <numeric>

class Solution {
public:
    bool canPartition(std::vector<int>& nums) {
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        if ((sum&1) == 1) {
            return false;
        }
        
        int n = sum/2;
        std::vector<int> dp(n+1, 0);
        dp[0] = 1;

        for(int i = 0; i < nums.size(); i++) {
            for(int j = n; j >= nums[i]; j--) {
                dp[j] = max(dp[j], dp[j-nums[i]]);
            }
            if (dp[n] > 0) {
                return true;
            }
        }
        return false;
    }
};
// @lc code=end

