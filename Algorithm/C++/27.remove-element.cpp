/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start

#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int left = 0, right = 0;
        while (right < nums.size()) {
            if (nums[right] != val) {
                nums[left] = nums[right];
                left++;
            }
            right++;
        }
        return left;
    }
};
// @lc code=end

