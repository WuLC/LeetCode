# -*- coding: utf-8 -*-
# Created on Sun Oct 29 2017 10:50:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# one pointer
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        while idx < len(bits) - 1:
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2
        return True if idx == len(bits) - 1 else False