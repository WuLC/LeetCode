# -*- coding: utf-8 -*-
# Created on Tue Jan 29 2019 23:47:0
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        s = ''
        while A > 0 or B > 0:
            if A == B:
                s += 'ab'*A
                break
            elif A > B:
                s += 'aa' if A > 1 else 'a'
                A -= 2
                s += 'b' if B > 0 else ''
                B -= 1
            else:
                s += 'bb' if B > 1 else 'b'
                B -= 2
                s += 'a' if A > 0 else ''
                A -= 1
        return s