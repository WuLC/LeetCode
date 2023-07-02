#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        covered = 0
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= right or intervals[i][0] == left:
                covered += 1
            if intervals[i][1] > right:
                left, right = intervals[i]
        return len(intervals) - covered
        
# @lc code=end

