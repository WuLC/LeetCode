# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-08-20 11:36:13
# @Last Modified by:   LC
# @Last Modified time: 2017-08-20 11:36:24



class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M) == 0:
            return []
        m, n = len(M), len(M[0])
        result = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                count, num = 0, 0
                for p in xrange(-1, 2):
                    for q in xrange(-1, 2):
                        if 0 <= i + p < m and 0 <= j + q < n:
                            num += 1;
                            count += M[i+p][j+q]
                result[i][j] = count/num
        return result