/*
 * @lc app=leetcode id=78 lang=cpp
 *
 * [78] Subsets
 */

// @lc code=start

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        result.clear();
        candidate.clear();
        dfs(nums, 0);
        return result;
    }

private:
    void dfs(std::vector<int>& nums, int idx) {
        result.push_back(candidate);
        if (idx == nums.size()) return;
        for (int i = idx; i < nums.size(); i++) {
            candidate.push_back(nums[i]);
            dfs(nums, i+1);
            candidate.pop_back();
        }
    }

    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
};
// @lc code=end

