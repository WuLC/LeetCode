# -*- coding: utf-8 -*-
# Created on Mon Jan 14 2019 18:56:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# heap queue 

import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        result = []
        for p in points:
            if len(result) < K:
                heapq.heappush(result, (-(p[0]**2 + p[1]**2), p)) # can't use result.append(-(p[0]**2 + p[1]**2), p) in ordre to heapify the 
            else:
                heapq.heappushpop(result, (-(p[0]**2 + p[1]**2), p))
        return map(lambda x: x[1], result)