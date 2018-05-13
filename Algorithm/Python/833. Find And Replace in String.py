# -*- coding: utf-8 -*-
# Created on Sun May 13 2018 11:28:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers and hash map
class Solution(object):
    def findReplaceString(self, S, idxs, sources, targets):
        """
        :type S: str
        :type idxs: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        mapping = {}
        for i in xrange(len(idxs)):
            n = len(sources[i])
            if S[idxs[i]:idxs[i]+n] == sources[i]:
                mapping[idxs[i]] = [sources[i], targets[i]]
        order = sorted(mapping.items())
        start, end = 0, 0
        result = ""
        for o in order:
            end = o[0]
            result += S[start:end]
            result += o[1][1]
            start = end + len(o[1][0])
        result += S[start:]
        return result