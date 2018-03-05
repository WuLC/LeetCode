# -*- coding: utf-8 -*-
# Created on Tue Feb 20 2018 14:36:46
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.lower()
        result = ['']
        for ch in S:
            next = [r + ch for r in result]
            if ch.islower():
                next += [r + ch.upper() for r in result]
            result = next
        return result