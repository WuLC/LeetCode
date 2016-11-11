# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-11 07:42:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-11 08:00:33
# @Email: liangchaowu5@gmail.com


# sort and greedy
# traverse the ballones, shrink the range of the one-shot-balloons with smaller end and larger start
# start a new one-shot-balloons when the start of current balloon is no smaller than the end of the previous one-shot-balloons
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def compare(x,y):
            return x[1]-y[1] if x[0]==y[0] else x[0]-y[0]
        points.sort(cmp = compare)
        start, end, count = None, None, 0 # start and end represent a one-shot-balloons
        for point in points:
            if end == None or point[0] > end:
                count += 1
                start, end = point
            else:
                start = max(start, point[0])
                end = min(end, point[1])
        return count