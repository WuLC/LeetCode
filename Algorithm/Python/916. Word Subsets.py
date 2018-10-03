# -*- coding: utf-8 -*-
# Created on Wed Oct 03 2018 10:49:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
from collections import defaultdict, Counter
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        max_freq = defaultdict(int)
        for word in B:
            count = Counter(word)
            for k, v in count.items():
                max_freq[k] = max(max_freq[k], v)
        result = []
        for word in A:
            legal = True
            count = Counter(word)
            for k, v in max_freq.items():
                if max_freq[k] > count[k]:
                    legal = False
                    break
            if legal:
                result.append(word)
        return result