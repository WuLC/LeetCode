/*
 * @lc app=leetcode id=77 lang=cpp
 *
 * [77] Combinations
 */

// @lc code=start

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> result;
        std::vector<int> candidate;
        backtrack(result, candidate, n, k, 1);
        return result;
    }
    
    void backtrack(std::vector<std::vector<int>>& result, std::vector<int>& candidate, int n, int k, int idx) {
        if (candidate.size() == k) {
            std::vector<int> tmp(candidate);
            result.push_back(tmp);
            return;
        }
        for (int i = idx; i <= n; i++) {
            candidate.push_back(i);
            backtrack(result, candidate, n, k, i+1);
            candidate.pop_back();
        }
        return;
    }
};
// @lc code=end

