# -*- coding: utf-8 -*-
# Created on Wed Feb 14 2018 2:7:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# hashmap
from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        result = 0
        cnt = Counter(answers)
        for k, v in cnt.items():
            result += (k+1) * int(math.ceil(v*1.0/(k+1)))
        return result