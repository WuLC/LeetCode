/*
 * @lc app=leetcode id=1005 lang=cpp
 *
 * [1005] Maximize Sum Of Array After K Negations
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int largestSumAfterKNegations(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < 0 and k > 0) {
                nums[i] *= -1;
                k--;
            }
        }

        if (k%2 > 0) {
            std::sort(nums.begin(), nums.end());
            nums[0] *= -1;
        }
        return std::accumulate(nums.begin(), nums.end(), 0);
    }
};
// @lc code=end

