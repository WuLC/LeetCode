/*
 * @lc app=leetcode id=1288 lang=cpp
 *
 * [1288] Remove Covered Intervals
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int removeCoveredIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), 
            [](const std::vector<int>& v1, const std::vector<int>& v2){
                if (v1[0] != v2[0]) {
                    return v1[0] < v2[0];
                } else {
                    return v1[1] < v2[1];
                }
        });

        int covered = 0;
        int left = intervals[0][0], right = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][1] <= right || intervals[i][0] == left) covered++;
            if (intervals[i][1] > right) {
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        return intervals.size() - covered;
    }
};
// @lc code=end

