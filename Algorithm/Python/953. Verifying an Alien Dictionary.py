# -*- coding: utf-8 -*-
# Created on Fri Dec 14 2018 14:15:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# compare char by char, pay attention to the case when one word is the prefix of another word
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_num = {}
        for i, c in enumerate(order):
            order_num[c] = i
        for i in xrange(len(words) - 1):
            equal = True
            for j in xrange(min(len(words[i]), len(words[i+1]))):
                if order_num[words[i][j]] < order_num[words[i+1][j]]:
                    equal = False
                    break
                elif order_num[words[i][j]] > order_num[words[i+1][j]]:
                    return False
            if equal and len(words[i]) > len(words[i+1]):
                return False
        return True