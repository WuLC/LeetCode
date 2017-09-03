# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-03 10:29:53
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-03 10:33:33

# traverse from left to right
# for each digit, find the largest digit after it and swap
# if there are duplicate largest digit, swap the last one 
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = [c for c in str(num)]
        for i in xrange(len(s)):
            idx = None
            for j in xrange(i+1, len(s)):
                if s[i] < s[j]:
                    if idx == None or s[j] >= s[idx]:
                        idx = j
            if idx != None:
                s[i], s[idx] = s[idx], s[i]
                return int(''.join(s))
        return num