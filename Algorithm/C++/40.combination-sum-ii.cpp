/*
 * @lc app=leetcode id=40 lang=cpp
 *
 * [40] Combination Sum II
 */

// @lc code=start
#include <vector>


class Solution {
public:
    std::vector<std::vector<int>> combinationSum2(std::vector<int>& nums, int target) {
        result.clear();
        candidate.clear();
        curr_sum = 0;
        std::vector<int> used(nums.size(), 0);
        std::sort(nums.begin(), nums.end());
        backtrack(nums, target, 0, used);
        return result;
    }

private:
    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
    int curr_sum;
    
    void backtrack(std::vector<int>& nums, int target, int idx, std::vector<int>& used) {
        if (curr_sum == target) {
            result.push_back(candidate);
            return;
        }

        for(int i = idx; i < nums.size(); i++) {
            if (curr_sum + nums[i] > target) return; // pruning
            if (i > 0 && nums[i] == nums[i-1] && used[i-1] == 0) continue; // de-duplicate
            curr_sum += nums[i];
            candidate.push_back(nums[i]);
            used[i] = 1;
            backtrack(nums, target, i+1, used);
            candidate.pop_back();
            curr_sum -= nums[i];
            used[i] = 0;
        }
    }
};
// @lc code=end

