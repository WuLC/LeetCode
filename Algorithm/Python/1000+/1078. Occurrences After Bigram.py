# -*- coding: utf-8 -*-
# Created on Sun Jun 09 2019 17:19:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        return [words[i+2] for i in xrange(len(words)-2) if words[i] == first and words[i+1] == second]
        