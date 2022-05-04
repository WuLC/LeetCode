/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target) {
        int mid, left = 0, right = nums.size() - 1;
        while(left <= right) {
            mid = left + ((right - left) >> 1);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
// @lc code=end

