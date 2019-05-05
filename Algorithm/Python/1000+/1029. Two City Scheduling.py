# -*- coding: utf-8 -*-
# Created on Sun May 05 2019 10:9:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        diff = [(costs[i][1] - costs[i][0], i) for i in xrange(n)]
        result = 0
        for i, e in enumerate(sorted(diff)):
            if i < (n>>1):
                result += costs[e[1]][1]
            else:
                result += costs[e[1]][0]
        return result
        