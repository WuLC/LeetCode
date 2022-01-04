/*
 * @lc app=leetcode id=503 lang=cpp
 *
 * [503] Next Greater Element II
 */

// @lc code=start

#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> nextGreaterElements(std::vector<int>& nums) {
        std::vector<int> result(nums.size(), -1);
        std::stack<int> s;        
        for (int _iter=0; _iter < 2; _iter++) {
            for (int i = 0; i < nums.size(); i++) {
                while (!s.empty() && nums[s.top()] < nums[i]) {
                    if (result[s.top()] == -1) {
                        result[s.top()] = nums[i];
                    }
                    s.pop();
                }
                s.push(i);
            }
        }
        return result;
    }
};
// @lc code=end

