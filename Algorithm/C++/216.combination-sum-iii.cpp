/*
 * @lc app=leetcode id=216 lang=cpp
 *
 * [216] Combination Sum III
 */

// @lc code=start

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum3(int k, int n) {
        curr_sum = 0;
        result.clear();
        candidate.clear();
        backtrack(k, n, 1);
        return result;
    }

private:
    std::vector<std::vector<int>> result;
    std::vector<int> candidate;
    int curr_sum;

    void backtrack(int k, int n, int idx) {
        if (candidate.size() == k) {
            if (curr_sum == n) result.push_back(candidate);
            return;
        }
        for(int i = idx; i <= 9; i++) {
            if (curr_sum+i > n) return; // pruning
            curr_sum += i;
            candidate.push_back(i);
            backtrack(k, n, i+1);
            curr_sum -= i;
            candidate.pop_back();
        }
    }


};
// @lc code=end

