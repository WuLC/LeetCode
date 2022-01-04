/*
 * @lc app=leetcode id=739 lang=cpp
 *
 * [739] Daily Temperatures
 */

// @lc code=start
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        std::vector<int> result(temperatures.size(), 0);
        std::stack<int> idx;
        for (int i=0; i < temperatures.size(); i++) {
            while(idx.size() > 0 && temperatures[i] > temperatures[idx.top()]) {
                result[idx.top()] = i;
                idx.pop();
            }
            idx.push(i);
        }
        return result;
    }
};
// @lc code=end

