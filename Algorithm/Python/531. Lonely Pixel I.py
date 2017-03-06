# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-06 15:31:24
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-06 15:36:03
# @Email: liangchaowu5@gmail.com


# O(n^2) time, O(n) space
# record the rows which has only one black pixel and its corresponding col index
# then check whether the corresponding column has only one black pixel

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if len(picture) == 0:
            return 0
        result = 0
        m, n = len(picture), len(picture[0])
        col_count = [0 for _ in xrange(n)]
        cols = []
        for i in xrange(m):
            col_idx = None
            black_count = 0
            for j in xrange(n):
                if picture[i][j] == 'B':
                    black_count += 1
                    col_idx = j
                    col_count[j] += 1
            if black_count == 1:
                cols.append(col_idx)
        for col in cols:
            if col_count[col] == 1:
                result += 1
        return result