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
        if ((sum&1) == 1) return false;
        
        int m = nums.size(), n = sum>>1;
        std::vector<std::vector<bool>> dp(m+1, std::vector<bool>(n+1, false));

        for(int i=1; i<=m; i++) {
            for(int j=0; j<=n; j++) {
                if (nums[i-1] > n) return false;
                if (nums[i-1] == n) return true;
                if (j==0) {
                    dp[i][j] = true;
                    continue;
                }

                dp[i][j] = dp[i-1][j] || (j >= nums[i-1] && dp[i-1][j-nums[i-1]]);
                if (dp[i][n]) return true;
            }
        }
        return false;                 
    }
};
// @lc code=end

