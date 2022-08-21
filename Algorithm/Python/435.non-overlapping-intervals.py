#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        def comparator(x1, x2):
            if x1[0] == x2[0]:
                return x1[1] - x2[1]
            else:
                return x1[0] - x2[0]

        intervals.sort(cmp = comparator)

        start, end = intervals[0]
        result = 0
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < end:
                result += 1
                if e < end:
                    start, end = s, e
            else:
                start, end = s, e
        return result

# @lc code=end

