# -*- coding: utf-8 -*-
# Created on Sun Nov 11 2018 11:25:8
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# create index with hashmap
from collections import defaultdict
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_idx = defaultdict(set)
        area = 1600000001
        for x, y in points:
            x_idx[x].add(y)
        xs = sorted(x_idx.keys())
        for i in xrange(len(xs)):
            for j in xrange(i + 1, len(xs)):
                legal_y = sorted([key for key in x_idx[xs[i]] if key in x_idx[xs[j]]])
                if len(legal_y) > 1:
                    min_y = min(legal_y[k+1] - legal_y[k] for k in xrange(len(legal_y) - 1))
                    area = min(area, (xs[j] - xs[i]) * min_y)
        return area if area != 1600000001 else 0