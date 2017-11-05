# -*- coding: utf-8 -*-
# Created on Sun Nov 05 2017 13:8:57
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# hashtable
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        count = {}
        for word in words:
            n = len(word)
            count.setdefault(n, set())
            count[n].add(word)
        sorted_count = sorted(count.items(), key = lambda item:item[0])
        idx, i = 1, 0
        while i < len(sorted_count):
            if idx != sorted_count[i][0]:
                break
            idx += 1
            i += 1
        for i in reversed(xrange(min(idx, sorted_count[-1][0]))):
            ws = sorted(list(sorted_count[i][1]))
            for w in ws:
                valid = True
                for j in xrange(len(w)):
                    if j+1 not in count or w[:j+1] not in count[j+1]:
                        valid = False
                        break
                if valid:
                    return w
        return ''
        
            
            
        