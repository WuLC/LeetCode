# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-02-13 16:25:52
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-13 16:26:34
# @Email: liangchaowu5@gmail.com


# hashmap, O(mn) space
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        result = []
        count = collections.defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                count[i+j].append(matrix[i][j])
        
        for i in xrange(m+n-1):
            result += count[i][::-1] if i&1 == 0 else count[i]
        return result
        
        