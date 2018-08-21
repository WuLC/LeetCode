# -*- coding: utf-8 -*-
# Created on Tue Aug 21 2018 9:27:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two hashmap
from collections import defaultdict
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(w, p):
            if len(w) != len(p):
                return False
            m1, m2 = {}, {}
            for i in xrange(len(w)):
                if w[i] in m1 and p[i] in m2:
                    if m1[w[i]] != p[i] or m2[p[i]] != w[i]:
                        return False
                elif w[i] not in m1 and p[i] not in m2:
                    m1[w[i]] = p[i]
                    m2[p[i]] = w[i]
                else:
                    return False
            return True
        result = []
        for word in words:
            if match(word, pattern):
                result.append(word)
        return result