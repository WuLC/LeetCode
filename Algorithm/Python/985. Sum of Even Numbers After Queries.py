# -*- coding: utf-8 -*-
# Created on Sun Feb 03 2019 17:18:14
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        tmp = sum(num for num in A if (num&1) == 0)
        for v, i in queries:
            if A[i]&1 == 0 and v&1 == 0:
                tmp += v
            elif A[i]&1 == 1 and v&1 == 1:
                tmp += A[i] + v
            elif A[i]&1 == 0 and v&1 == 1:
                tmp -= A[i]
            result.append(tmp)
            A[i] += v
        return result