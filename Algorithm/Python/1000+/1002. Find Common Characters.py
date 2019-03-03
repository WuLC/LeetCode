# -*- coding: utf-8 -*-
# Created on Sun Mar 03 2019 10:31:27
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# simple solution
from collections import Counter


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counters = [Counter(s) for s in A]
        result = []
        for k, v in counters[0].items():
            for i in xrange(1, len(A)):
                v = min(v, counters[i][k])
            result += [k] * v
        return result
