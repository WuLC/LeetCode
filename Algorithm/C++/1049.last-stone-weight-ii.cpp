/*
 * @lc app=leetcode id=1049 lang=cpp
 *
 * [1049] Last Stone Weight II
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    int lastStoneWeightII(std::vector<int>& stones) {
        int sum = std::accumulate(stones.begin(), stones.end(), 0);
        int n = sum>>1;
        std::vector<int> dp(n+1, 0);
        for (int i = 0; i < stones.size(); i++) {
            for (int j = n; j >= stones[i]; j--) {
                dp[j] = std::max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }
        return sum - dp[n] - dp[n];
    }
};
// @lc code=end

