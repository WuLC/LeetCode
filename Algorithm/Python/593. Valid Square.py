# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-21 15:20:45
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-21 15:23:10
# @Email: liangchaowu5@gmail.com


# judge if there are only two kinds of length between points
# pay attention that same points may appear
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def distance(point1, point2):
            return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
        all_dist = set()
        points = [p1, p2, p3, p4]
        for i in xrange(len(points)):
            for j in xrange(i+1, len(points)):
                all_dist.add(distance(points[i], points[j]))
        return len(all_dist) == 2 and 0 not in all_dist
        