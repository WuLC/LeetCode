/*
 * @lc app=leetcode id=283 lang=cpp
 *
 * [283] Move Zeroes
 */

// @lc code=start

#include <vector>

class Solution {
public:
    void moveZeroes(std::vector<int>& nums) {
        int tmp, left = 0, right = 0;
        while (right < nums.size()) {
            if (nums[right] != 0) {
                tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
                left++;
            }
            right++;
        }
    }
};
// @lc code=end

