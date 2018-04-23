# -*- coding: utf-8 -*-
# Created on Mon Apr 23 2018 12:24:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# reverse words and sort, check if a word if the prefix of its next word
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sorted_words = sorted([word[::-1] for word in words])
        n = len(sorted_words)
        result, count = 0, 0
        for i in xrange(n):
            if i != n-1 and sorted_words[i] == sorted_words[i+1][:len(sorted_words[i])]:
                continue
            result += len(sorted_words[i])
            count += 1
        return result+count