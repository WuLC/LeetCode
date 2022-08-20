#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def comparator(x1, x2):
            if x1[0] == x2[0]:
                return x1[1] - x2[1]
            else:
                return x1[0] - x2[0]      
        points.sort(cmp=comparator)

        start, end, result = None, None, 0
        for i in range(len(points)):
            if end is None or points[i][0] > end:
                start, end = points[i]
                result += 1
            start = max(start, points[i][0])
            end = min(end, points[i][1])
        return result

            
# @lc code=end

