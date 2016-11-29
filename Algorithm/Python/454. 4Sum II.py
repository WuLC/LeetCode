# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-11-29 13:18:50
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-29 13:24:06
# @Email: liangchaowu5@gmail.com


# hashtable,O(n^2) time, O(n^2) space
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result, n = 0, len(A)
        if n == 0:
            return result
        sum_count = collections.defaultdict(int)
        for i in xrange(n):
            for j in xrange(n):
                sum_count[ A[i] + B[j] ] += 1
        
        for i in xrange(n):
            for j in xrange(n):
                tmp = C[i] + D[j]
                result += sum_count[-tmp]
        return result
        