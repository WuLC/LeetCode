/*
 * @lc app=leetcode id=496 lang=cpp
 *
 * [496] Next Greater Element I
 */

// @lc code=start
#include <vector>
#include <stack>
#include <unordered_map>

class Solution {
public:
    std::vector<int> nextGreaterElement(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::vector<int> result(nums1.size(), -1);
        std::unordered_map<int, int> idx_map;
        for (int i = 0; i < nums1.size(); i++) {
            idx_map[nums1[i]] = i;
        }
        std::stack<int> s;
        for (auto num : nums2) {
            while (!s.empty() && s.top() < num) {
                if (idx_map.find(s.top()) != idx_map.end()) {
                    result[idx_map[s.top()]] = num;
                }
                s.pop();
            }
            s.push(num);
        }
        return result;
    }
};
// @lc code=end

