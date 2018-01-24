# -*- coding: utf-8 -*-
# Created on Wed Jan 24 2018 16:57:37
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# hash table
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mapping = {}
        for i in xrange(len(B)):
            mapping[B[i]] = i
        return [mapping[num] for num in A]