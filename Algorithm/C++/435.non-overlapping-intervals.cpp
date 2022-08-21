/*
 * @lc app=leetcode id=435 lang=cpp
 *
 * [435] Non-overlapping Intervals
 */

// @lc code=start

#include <vector>
#include <algorithm>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& v1, const std::vector<int>& v2) -> bool {
            if (v1[0] != v2[0]) {
                return v1[0] < v2[0];
            } else {
                return v1[1] < v2[1];
            }
        });
        

        int pre_end = intervals[0][1], result = 0;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < pre_end) {
                result++;
                if (intervals[i][1] < pre_end) {
                    pre_end = intervals[i][1];
                }
            } else {
                pre_end = intervals[i][1];
            }
        }
        return result;
    }
};
// @lc code=end

