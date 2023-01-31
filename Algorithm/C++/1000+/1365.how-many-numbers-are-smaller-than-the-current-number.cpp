/*
 * @lc app=leetcode id=1365 lang=cpp
 *
 * [1365] How Many Numbers Are Smaller Than the Current Number
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> smallerNumbersThanCurrent(std::vector<int>& nums) {
        std::vector<int> original_nums(nums);
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, int> counter;
        for (int i = 0; i < nums.size(); i++) {
            if (counter.find(nums[i]) == counter.end()) {
                counter[nums[i]] = i;
            }
        }
        std::vector<int> result;
        result.reserve(nums.size());
        for (int num: original_nums) {
            result.push_back(counter[num]);
        }
        return result;
    }
};
// @lc code=end

