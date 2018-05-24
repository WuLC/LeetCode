# -*- coding: utf-8 -*-
# Created on Thu May 24 2018 9:47:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# judge the case when they do not overlap
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1]:
            return False
        return True