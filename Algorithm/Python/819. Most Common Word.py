# -*- coding: utf-8 -*-
# Created on Mon Apr 16 2018 22:34:30
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, check char by char
from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        result, tmp = '', 0
        count = defaultdict(int)
        start, i = 0, 0
        while i <= len(paragraph):
            if i==len(paragraph) or not paragraph[i].isalpha():
                if i - start > 0:
                    word = paragraph[start:i].lower()
                    if word not in banned:
                        count[word] += 1
                        if count[word] > tmp:
                            result = word
                            tmp = count[word]
                while i < len(paragraph) and not paragraph[i].isalpha():
                    i += 1
                start = i
            i += 1
        return result          