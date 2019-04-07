# -*- coding: utf-8 -*-
# Created on Sun Apr 07 2019 20:56:32
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# be careful of overflow with too many bits
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        curr = 0
        for num in A:
            curr = (curr * 2 + num) % 5
            if curr == 0:
                result.append(True)
            else:
                result.append(False)
        return result
                