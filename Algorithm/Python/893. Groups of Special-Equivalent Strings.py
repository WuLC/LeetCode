# -*- coding: utf-8 -*-
# Created on Sat Sep 15 2018 11:40:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        candidate = set()
        for s in A:
            odd, even = [], []
            for i in xrange(len(s)):
                if i%2:
                    odd.append(s[i])
                else:
                    even.append(s[i])
            candidate.add(''.join(sorted(odd)) + '_' + ''.join(sorted(even)))
        return len(candidate)
        