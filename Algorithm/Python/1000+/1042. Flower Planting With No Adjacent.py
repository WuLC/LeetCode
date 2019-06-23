# -*- coding: utf-8 -*-
# Created on Sat Jun 22 2019 10:27:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        conns = [set() for _ in xrange(N+1)]
        for n1, n2 in paths:
            conns[n1-1].add(n2-1)
            conns[n2-1].add(n1-1)
        colors = [0] * N
        for i in xrange(N):
            colors[i] = ({1, 2, 3, 4} - {colors[t] for t in conns[i]}).pop()
        return colors
