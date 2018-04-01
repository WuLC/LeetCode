# -*- coding: utf-8 -*-
# Created on Sun Apr 01 2018 11:12:55
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pointers
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if self.__is_stretchy(word, S):
                count += 1
        return count
    
    def __is_stretchy(self, word, s):
        p1, p2 = 0, 0
        while p1 < len(word) and p2 < len(s):
            c1, c2 = 1, 1
            while p1+1 < len(word) and word[p1] == word[p1+1]:
                c1 += 1
                p1 += 1
            while p2+1 < len(s) and s[p2] == s[p2+1]:
                c2 += 1
                p2 += 1
            if word[p1] != s[p2] or c1 > c2 or (c2 < 3 and c1 != c2):
                return False
            if p1+1 == len(word) and p2+1 == len(s):
                return True
            p1 += 1
            p2 += 1
        return False
                
            