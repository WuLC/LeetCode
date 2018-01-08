# -*- coding: utf-8 -*-
# Created on Mon Jan 08 2018 21:8:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# math 
# referer: https://discuss.leetcode.com/topic/115531/c-o-1-solution-without-loop

import math
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = int(math.ceil((-1 + math.sqrt(1 + 8*target))/2))
        total = n*(n+1)/2
        if total == target:
            return n
        diff = total - target
        if (diff&1)== 0:
            return n
        elif (n&1) == 0:
            return n+1
        else:
            return n+2
        