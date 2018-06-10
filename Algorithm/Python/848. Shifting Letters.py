# -*- coding: utf-8 -*-
# Created on Sun Jun 10 2018 21:39:20
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# use ascii code
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        curr = 0
        for i in reversed(xrange(len(shifts))):
            shifts[i] += curr
            curr = shifts[i]
        ascii = []
        for i in xrange(len(S)):
            ascii.append((ord(S[i])-97+shifts[i])%26)
        return ''.join(chr(num+97) for num in ascii)