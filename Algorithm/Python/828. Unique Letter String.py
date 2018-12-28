# -*- coding: utf-8 -*-
# Created on Thu Dec 27 2018 16:10:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        result = 0
        MOD = 1000000007
        for i in xrange(len(S)):
            left, right = i - 1, i + 1
            while left >=0 and S[left] != S[i]:
                left -= 1
            while right < len(S) and S[right] != S[i]:
                right += 1
            result += ((i - left) * (right - i)) % MOD
            result %= MOD
        return result
            