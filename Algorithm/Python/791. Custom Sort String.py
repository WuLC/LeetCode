# -*- coding: utf-8 -*-
# Created on Tue Mar 06 2018 21:16:57
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap
from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ''
        count = Counter(T)
        for c in S:
            if c in count:
                result += c*count[c]
                count[c] = 0
        for c in count:
            result += c*count[c]
        return result
        
        