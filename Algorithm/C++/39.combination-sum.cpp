/*
 * @lc app=leetcode id=39 lang=cpp
 *
 * [39] Combination Sum
 */

// @lc code=start
#include <vector>


class Solution {
public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& nums, int target) {
        result.clear();
        candidate.clear();
        curr_sum = 0;
        std::sort(nums.begin(), nums.end());
        backtrack(nums, target, 0);
        return result;
    }

private:
    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
    int curr_sum;
    
    void backtrack(std::vector<int>& nums, int target, int idx) {
        if (curr_sum == target) {
            result.push_back(candidate);
            return;
        }

        for(int i = idx; i < nums.size(); i++) {
            if (curr_sum + nums[i] > target) return; // pruning
            curr_sum += nums[i];
            candidate.push_back(nums[i]);
            backtrack(nums, target, i);
            candidate.pop_back();
            curr_sum -= nums[i];
        }
    }
};
// @lc code=end

