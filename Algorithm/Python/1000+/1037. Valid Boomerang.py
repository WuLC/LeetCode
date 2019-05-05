# -*- coding: utf-8 -*-
# Created on Sun May 05 2019 15:46:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        p1, p2, p3 = points
        return (p2[1] - p1[1]) * (p3[0] - p2[0]) != (p2[0] - p1[0]) * (p3[1] - p2[1])