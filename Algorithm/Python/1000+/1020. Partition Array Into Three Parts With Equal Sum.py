# -*- coding: utf-8 -*-
# Created on Sun Mar 24 2019 22:2:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        tmp, count, ave = 0, 0, s/3
        for i in xrange(len(A)):
            if tmp == ave:
                tmp = 0
                count += 1
            tmp += A[i]
        if tmp == ave:
            count += 1
        return True if count == 3 else False
