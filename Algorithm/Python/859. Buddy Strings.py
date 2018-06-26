# -*- coding: utf-8 -*-
# Created on Tue Jun 26 2018 20:45:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution 
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        diff_idx = []
        chars = set()
        repeat_char = False
        for i in xrange(len(A)):
            if A[i] in chars:
                repeat_char = True
            chars.add(A[i])
            if A[i] != B[i]:
                diff_idx.append(i)
        return (repeat_char and len(diff_idx) == 0) or \
               (len(diff_idx) == 2 and A[diff_idx[0]] == B[diff_idx[1]] and A[diff_idx[1]] == B[diff_idx[0]])