/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int left = 0, right = 1;
        while (right < nums.size()) {
            if (nums[right] != nums[left]){
                left++;
                nums[left] = nums[right];
            }
            right++;
        }
        return std::min(left + 1, int(nums.size()));
    }
};
// @lc code=end

