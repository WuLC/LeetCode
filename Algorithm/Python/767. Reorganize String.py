# -*- coding: utf-8 -*-
# Created on Tue Jan 23 2018 21:49:1
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap, 
# if (length of the longest character) - (total length of the rest characters) <= 1 than it is possible to reorganize
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = Counter(S)
        sorted_count = sorted(count.items(), key=lambda x:-x[1])
        max_len = sorted_count[0][1]
        if max_len * 2 - sum((s[1] for s in sorted_count)) > 1:
            return ''
        result = [''] * max_len
        idx = 0
        for s in sorted_count:
            for j in xrange(s[1]):
                result[idx%max_len] += s[0]
                idx += 1
        return ''.join(result)
        