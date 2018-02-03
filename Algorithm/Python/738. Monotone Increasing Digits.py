# -*- coding: utf-8 -*-
# Created on Sat Feb 03 2018 21:52:53
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution 
# find the first index that N[idx] > N[idx+1]
# then keep doing idx -= 1 while N[idx] == N[idx-1]
# finally make N[idx] -= 1 and keep all digits after it as 9
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        idx = None
        for i in xrange(len(s) - 1):
            if s[i] > s[i+1]:
                idx = i
                break
        if idx == None:
            return N
        else:
            while idx > 0 and s[idx] == s[idx-1]:
                idx -= 1
            return int(s[:idx] + str(int(s[idx])-1) + '9'*(len(s) - idx - 1))