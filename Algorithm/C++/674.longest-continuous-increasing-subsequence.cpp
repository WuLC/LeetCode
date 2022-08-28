/*
 * @lc app=leetcode id=674 lang=cpp
 *
 * [674] Longest Continuous Increasing Subsequence
 */

// @lc code=start

#include <vector>

class Solution {
public:
    int findLengthOfLCIS(std::vector<int>& nums) {
        int curr_len = 1, result = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                curr_len++;
            } else {
                curr_len = 1;
            }
            result = std::max(result, curr_len);
        }
        return result;
    }
};
// @lc code=end

