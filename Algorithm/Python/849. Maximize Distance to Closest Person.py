# -*- coding: utf-8 -*-
# Created on Sun Jun 10 2018 17:30:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution 
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        idx = []
        for i in xrange(len(seats)):
            if seats[i] == 1:
                idx.append(i)
        result = max(idx[0], len(seats)-idx[-1]-1)
        for i in xrange(len(idx)-1):
            result = max(result, (idx[i+1]-idx[i])//2)
        return result