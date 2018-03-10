# -*- coding: utf-8 -*-
# Created on Sat Mar 10 2018 16:4:34
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap to record position 
from collections import defaultdict
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        indices = defaultdict(list)
        for i in xrange(len(S)):
            indices[S[i]].append(i)
        count=0
        for word in words:
            record = {k:0 for k in indices.keys()}
            legal, idx = True, -1
            for c in word:
                if c not in indices or record[c] == len(indices[c]) or idx > indices[c][-1]:
                    legal = False
                    break
                for i in xrange(record[c], len(indices[c])):
                    if idx > indices[c][i]:
                        continue
                    else:
                        idx = indices[c][i]
                        record[c] = i+1
                        break
            if legal:
                count += 1
        return count