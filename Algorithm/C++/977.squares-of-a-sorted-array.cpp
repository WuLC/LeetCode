/*
 * @lc app=leetcode id=977 lang=cpp
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start

#include <vector>

class Solution {
public:
    std::vector<int> sortedSquares(std::vector<int>& nums) {
        std::vector<int> result(nums.size(), 0);
        int left = 0, right = nums.size() - 1, left_sq, right_sq;
        for (int i = nums.size() - 1; i >= 0; i--) {
            left_sq = nums[left] * nums[left];
            right_sq = nums[right] * nums[right];
            if (left_sq > right_sq) {
                result[i] = left_sq;
                left++;
            } else {
                result[i] = right_sq;
                right--;
            }
        }
        return result;
    }
};
// @lc code=end

