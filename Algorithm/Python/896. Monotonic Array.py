# -*- coding: utf-8 -*-
# Created on Sun Sep 02 2018 23:18:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        diff = [A[i+1]-A[i] for i in xrange(len(A)-1)]
        if all(d>=0 for d in diff) or all(d<=0 for d in diff):
            return True
        return False