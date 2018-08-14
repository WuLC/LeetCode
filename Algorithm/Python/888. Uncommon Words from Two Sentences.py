# -*- coding: utf-8 -*-
# Created on Mon Aug 13 2018 17:13:17
# Author: WuLC
# EMail: liangchaowu5@gmail.com


from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        result = []
        counterA = Counter(A.split())
        counterB = Counter(B.split())
        for k, v in counterA.items():
            if v==1 and k not in counterB:
                result.append(k)
        for k, v in counterB.items():
            if v==1 and k not in counterA:
                result.append(k)
        return result
        