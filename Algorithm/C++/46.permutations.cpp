/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

// @lc code=start

#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        result.clear();
        candidate.clear();
        exist.clear();
        backtrack(nums);
        return result;
    }

private:
    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
    std::unordered_set<int> exist;

    void backtrack(std::vector<int>& nums) {
        if (candidate.size() == nums.size()) {
            result.push_back(candidate);
            return;
        }
        for (int num: nums) {
            if (exist.find(num) != exist.end()) continue;
        
            candidate.push_back(num);
            exist.insert(num);
            backtrack(nums);
            candidate.pop_back();
            exist.erase(num);
        }
    }

};
// @lc code=end

