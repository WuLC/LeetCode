/*
 * @lc app=leetcode id=90 lang=cpp
 *
 * [90] Subsets II
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsetsWithDup(std::vector<int>& nums) {
        result.clear();
        candidate.clear();
        std::sort(nums.begin(), nums.end());
        std::vector<bool> used(nums.size(), false);
        dfs(nums, used, 0);
        return result;
    }

private:
    void dfs(std::vector<int>& nums, std::vector<bool>& used, int idx) {
        result.push_back(candidate);
        for (int i = idx; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) {
                continue;
            }
            candidate.push_back(nums[i]);
            used[i] = true;
            dfs(nums, used, i+1);
            candidate.pop_back();
            used[i] = false;
        }
    }

    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
};
// @lc code=end

