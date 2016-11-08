# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-08 14:39:32
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-08 14:40:24
# @Email: liangchaowu5@gmail.com


# hashtable
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for p1 in points:
            tmp = {}
            for p2 in points:
                distance = pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1],2)
                tmp.setdefault(distance, 0)
                tmp[distance] += 1
            for v in tmp.values():
                result += v*(v-1)
        return result
                