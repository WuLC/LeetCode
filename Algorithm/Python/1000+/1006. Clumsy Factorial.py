# -*- coding: utf-8 -*-
# Created on Fri Mar 15 2019 16:2:9
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# simple solution, four numbers as a group

import math


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        positive = True
        while N > 0:
            if N - 4 >= 0:
                if positive:
                    tmp = math.floor(N * (N-1)/(N-2)) + (N-3)
                else:
                    tmp = math.floor(N * (N-1)/(N-2)) - (N-3)
            elif N == 3:
                tmp = math.floor(N * (N-1)/(N-2))
            elif N == 2:
                tmp = N * (N-1)
            else:
                tmp = N
            result += tmp if positive else -1*tmp
            positive = False
            N -= 4
        return int(result)
