# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-04 16:14:28
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-04 16:14:41
# @Email: liangchaowu5@gmail.com

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        for i in xrange(len(points)):
            tmp, col, duplicate = {}, 0, -1
            for j in xrange(i, len(points)):
                if points[i].x == points[j].x:
                    col += 1
                    result = max(col, result)
                    if points[i].y == points[j].y:
                        duplicate += 1
                else:
                    sloap = float(points[i].y-points[j].y)/(points[i].x-points[j].x)
                    tmp.setdefault(sloap, 1)
                    tmp[sloap] += 1
                    result = max(result,tmp[sloap])
            if duplicate:
                for k,v in tmp.items():
                    tmp[k] += duplicate
                    result = max(result, tmp[k])
        return result