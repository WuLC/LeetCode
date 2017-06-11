# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-09 17:33:49
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-09 17:34:19
# @Email: liangchaowu5@gmail.com


# naive dp, O(n) time, TLE
class Solution(object):
    
    def __init__(self):
        self.cache = [1]
        self.nonCon = [1]
        
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        m = len(self.cache)
        for i in xrange(m, num+1):
            if self.nonCon[i>>1]  == 1 and ( i&1 == 0 or (i>>1)&1 == 0):
                self.cache.append(self.cache[-1]+1)
                self.nonCon.append(1)
            else:
                self.cache.append(self.cache[-1])
                self.nonCon.append(0)
        return self.cache[num]


# 