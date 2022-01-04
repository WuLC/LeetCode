/*
 * @lc app=leetcode id=84 lang=cpp
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start
#include <vector>
#include <stack>

class Solution {
public:
    int largestRectangleArea(std::vector<int>& heights) {
        // construct dummy heights
        std::vector<int> dummy_heights(heights.size()+2, 0);
        for (int i = 0; i < heights.size(); i++) {
            dummy_heights[i+1] = heights[i];
        }

        int curr_height, result = 0;
        std::stack<int> s;
        for (int i = 0; i < dummy_heights.size(); i++) {
            while(s.size() > 0 && dummy_heights[s.top()] > dummy_heights[i]) {
                curr_height = dummy_heights[s.top()]; 
                s.pop();
                result = std::max(result, curr_height * (i - s.top() - 1));
            }
            s.push(i);
        }
        return result;
    }
};
// @lc code=end

