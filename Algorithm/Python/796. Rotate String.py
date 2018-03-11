# -*- coding: utf-8 -*-
# Created on Sun Mar 11 2018 11:33:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        for i in xrange(len(A)):
            if A[i:]+A[:i] == B:
                return True
        return False