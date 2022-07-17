/*
 * @lc app=leetcode id=491 lang=cpp
 *
 * [491] Increasing Subsequences
 */

// @lc code=start
#include<vector>
#include<unordered_set>

class Solution {
public:
    std::vector<std::vector<int>> findSubsequences(std::vector<int>& nums) {
        result.clear();
        candidate.clear();
        dfs(nums, 0);
        return result;
    }

private:
    std::vector<std::vector<int>> result;
    std::vector<int> candidate;

    void dfs(std::vector<int>& nums, int idx) {
        if (candidate.size() >= 2) {
            result.push_back(candidate);
        }
        std::unordered_set<int> used;
        for (int i = idx; i < nums.size(); i++) {
            if (used.find(nums[i]) != used.end()) {
                continue;
            }
            if (candidate.size() == 0 || (candidate.back() <= nums[i])) {
                candidate.push_back(nums[i]);
                used.insert(nums[i]);
                dfs(nums, i+1);
                candidate.pop_back();
            }
        }
    }
};
// @lc code=end

