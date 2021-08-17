/*
 * @lc app=leetcode id=452 lang=cpp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        auto cmp = [](std::vector<int>& v1, std::vector<int>& v2) -> bool {
            // 测试元素的位置，以及返回什么值会交换两个元素
            // std::cout << v1[0] << "," <<v2[0] << endl;
            // return true;
            if (v1[0] != v2[0]) return v1[0] < v2[0];
            else return v1[1] < v2[1];
        };
        std::sort(points.begin(), points.end(), cmp);
        int result = 1, left = points[0][0], right = points[0][1];
        for (int i=1; i < points.size(); i++) {
            if (points[i][0] <= right) {
                left = std::max(left, points[i][0]);
                right = std::min(right, points[i][1]);
            } else {
                result++;
                left = points[i][0];
                right = points[i][1];
            }
        }
        return result;
    }
};
// @lc code=end