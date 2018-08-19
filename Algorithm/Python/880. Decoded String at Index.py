# -*- coding: utf-8 -*-
# Created on Sat Aug 18 2018 12:36:26
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, O(1) space
# referer: https://leetcode.com/problems/decoded-string-at-index/discuss/156747/C++Python-O(N)-Time-O(1)-Space
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        idx, n = -1, 0
        while n < K:
            idx += 1
            c = S[idx]
            if c.isdigit():
                n *= int(c)
            else:
                n += 1

        for i in xrange(idx, -1, -1):
            if S[i].isdigit():
                n /= int(S[i])
                K %= n
            else:
                if K==0 or K==n:
                    return S[i]
                else:
                    n -= 1        