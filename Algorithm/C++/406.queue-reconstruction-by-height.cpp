/*
 * @lc app=leetcode id=406 lang=cpp
 *
 * [406] Queue Reconstruction by Height
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> reconstructQueue(std::vector<std::vector<int>>& people) {
        std::sort(people.begin(), people.end(), [](const std::vector<int>& x1, const std::vector<int>& x2) {
            if (x1[0] == x2[0]) {
                return x1[1] < x2[1];
            } else {
                return x2[0] < x1[0];
            }
        });
        
        int k, idx;
        for (int i = 0; i < people.size(); i++) {
            k = people[i][1];
            if (i > k) {
                idx = i;
                while (idx > k) {
                    std::swap(people[idx], people[idx-1]);
                    idx--;
                }
            }
        }
        return people;
    }
};
// @lc code=end

