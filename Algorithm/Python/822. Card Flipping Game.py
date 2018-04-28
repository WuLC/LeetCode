# -*- coding: utf-8 -*-
# Created on Sat Apr 28 2018 20:9:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
# if fronts[i] == backs[i], then this number can never be the result
# else choose the smallest number of fronts[i] and backs[i]
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = set()
        for i in xrange(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        for i in xrange(len(fronts)):
            if backs[i] in same or (fronts[i] not in same and fronts[i] < backs[i]):
                fronts[i], backs[i] = backs[i], fronts[i]
        result = 0
        fs = set(fronts)
        for i in xrange(len(backs)):
            if backs[i] != fronts[i] and backs[i] not in fs:
                result = backs[i] if result == 0 else min(result, backs[i])
        return result