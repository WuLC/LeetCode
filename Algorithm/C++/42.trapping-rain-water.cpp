/*
 * @lc app=leetcode id=42 lang=cpp
 *
 * [42] Trapping Rain Water
 */

// @lc code=start

#include <vector>
#include <stack>


class Solution {
public:
    int trap(std::vector<int>& height) {
        int bottom, result=0;
        std::stack<int> s;
        for (int i = 0; i < height.size(); i++) {
            while (s.size() > 0 && height[s.top()] <= height[i]) {
                bottom = height[s.top()];
                s.pop();
                if (s.size() > 0) {
                    result += (std::min(height[i], height[s.top()]) - bottom) * (i - s.top() - 1);
                }
            }
            s.push(i);
        }
        return result;
    }
};
// @lc code=end

