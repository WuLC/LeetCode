# -*- coding: utf-8 -*-
# Created on Sun Nov 26 2017 11:38:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# use set, O(n) space(n=len(pairs)), O(m) time(m=len(words1)=len(words2))
# pay attention that list can not be add to set since it is changeable, change it to tuple firstly
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        s = set()
        for pair in pairs:
            s.add(tuple(pair))
        for i in xrange(len(words1)):
            if words1[i] == words2[i] or (words1[i], words2[i]) in s or (words2[i], words1[i]) in s:
                continue
            else:
                return False
        return True