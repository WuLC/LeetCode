# -*- coding: utf-8 -*-
# Created on Mon Apr 30 2018 23:55:32
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# pay attention that same difficulty may have different profit
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        p = [0]*100001
        for i in xrange(len(difficulty)):
            p[difficulty[i]] = max(profit[i], p[difficulty[i]])  # same difficulty may have different profit
        curr_max = 0
        for i in xrange(1, len(p)):
            curr_max = max(curr_max, p[i])
            p[i] = curr_max
        return sum(p[worker[i]] for i in xrange(len(worker))) 