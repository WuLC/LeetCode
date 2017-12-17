# -*- coding: utf-8 -*-
# Created on Sun Dec 17 2017 11:30:5
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# pay attention to small details

from collections import defaultdict, Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        chars = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                chars[c.lower()] += 1
        
        words.sort(key = lambda x:len(x))
        for w in words:
            legal = True
            count = Counter(w.lower())
            for k, v in chars.items():
                if count[k] < v:
                    legal = False
                    break
            if legal:
                return w
            
        