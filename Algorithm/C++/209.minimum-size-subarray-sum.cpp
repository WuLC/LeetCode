/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
#include <vector>
#include <cmath>

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int left = 0, right = 0, curr_sum = 0, result = 0;
        while(right <= nums.size()) {
            while (curr_sum >= target) {
                if (result == 0) {
                    result = right - left;
                } else {
                    result = std::min(result, right - left);
                }
                curr_sum -= nums[left];
                left++;
            }
            if (right < nums.size()) {
                curr_sum += nums[right];
            }
            right++;
        }
        return result;
    }
};
// @lc code=end

