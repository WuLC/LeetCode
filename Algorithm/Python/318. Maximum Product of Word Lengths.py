# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-24 08:36:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-24 08:36:25
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n, result = len(words), 0
        bits = [0 for i in xrange(n)]
        for i in xrange(n):
            for ch in words[i]:
                bits[i] |= 1<<(ord(ch)-97)
                
        for i in xrange(n):
            for j in xrange(i+1,n):
                if bits[i]&bits[j] == 0:
                    result = max(result, len(words[i])*len(words[j]))
        return result
                    
                