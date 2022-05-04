/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start

#include <vector>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        return std::vector{findIdx(nums, target, true), findIdx(nums, target, false)};
    }

private:
    int findIdx(const std::vector<int>& nums, int target, bool first_idx) {
        int mid, left = 0, right = nums.size() - 1;
        if (left > right) {
            return -1;
        }
        while (left < right) {
            mid = left + ((right-left)>>1);
            if (nums[mid] == target) {
                if (first_idx) {
                    right = mid;
                } else {
                    if (mid + 1 < nums.size() && nums[mid+1] != target) {
                        left = mid;
                        break;
                    }
                    left = mid + 1;
                }
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        if (nums[left] != target) {
            return -1;
        } else {
            return left;
        }
    }
};
// @lc code=end

