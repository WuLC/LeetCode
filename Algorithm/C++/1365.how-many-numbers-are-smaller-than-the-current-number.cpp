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
        std::vector<int> vec(nums);
        std::sort(vec.begin(), vec.end());
        std::unordered_map<int, int> idx;
        for (int i = 0; i < vec.size(); i++) {
            if (idx.find(vec[i]) == idx.end()) {
                idx[vec[i]] = i;
            }
        }

        std::vector<int> result;
        result.reserve(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            result.push_back(idx[nums[i]]);
        }
        return result;
    }
};
// @lc code=end

