    # -*- coding: utf-8 -*-
# Created on Thu Jan 03 2019 9:58:51
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# recursive, 
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return range(10)
        result = []
        for i in xrange(1, 10):
            result += self.generate(str(i), N, K)
        return map(lambda x: int(x), result)

    def generate(self, pre_digit, N, K):
        if N == 1:
            return [pre_digit]
        tmp = []
        d = int(pre_digit)
        if d - K >= 0:
            tmp += [pre_digit + e for e in self.generate(str(d - K), N - 1, K)]
        if K != 0 and d + K < 10:
            tmp += [pre_digit + e for e in self.generate(str(d + K), N - 1, K)]
        return tmp