/*
 * @lc app=leetcode id=455 lang=cpp
 *
 * [455] Assign Cookies
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    int findContentChildren(std::vector<int>& g, std::vector<int>& s) {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());
        int g_idx = 0, s_idx = 0, result = 0;
        while (g_idx < g.size() && s_idx < s.size()) {
            if (g[g_idx] <= s[s_idx]) {
                g_idx++;
                result++;
            }
            s_idx++;
        }
        return result;
    }
};
// @lc code=end

