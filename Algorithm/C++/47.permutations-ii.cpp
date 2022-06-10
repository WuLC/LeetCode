/*
 * @lc app=leetcode id=47 lang=cpp
 *
 * [47] Permutations II
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        result.clear();
        tmp.clear();
        std::vector<bool> used(nums.size(), false);
        std::sort(nums.begin(), nums.end());
        dfs(nums, used, 0);
        return result;
    }

private:
    void dfs(std::vector<int>& nums, std::vector<bool>& used, int idx) {
        if (idx > 0 && nums[idx] == nums[idx-1] && !used[idx-1]) {
            return;
        }
        if (tmp.size() == nums.size()) {
            result.push_back(tmp);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
           if (!used[i]) {
               tmp.push_back(nums[i]);
               used[i] = true;
               dfs(nums, used, i);
               used[i] = false;
               tmp.pop_back();
           }
        }
    }
    std::vector<std::vector<int>> result;
    std::vector<int> tmp;

};
// @lc code=end

