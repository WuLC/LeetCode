# -*- coding: utf-8 -*-
# Created on Wed May 30 2018 10:28:41
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pointers, deal with range grouped by forces one by one
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        idx = [(i, dominoes[i]) for i in xrange(len(dominoes)) if dominoes[i] != '.']
        result = [c for c in dominoes]
        idx = [(-1, 'L')] + idx + [(len(dominoes), 'R')]
        for i in xrange(len(idx) - 1):
            j, lf = idx[i]
            k, rf = idx[i+1]
            if lf == rf:
                for m in xrange(j+1, k):
                    result[m] = lf
            elif lf == 'R' and rf == 'L':
                for m in xrange(j+1, k):
                    if m - j == k - m:
                        result[m] = '.'
                    elif m - j > k - m:
                        result[m] = 'L'
                    else:
                        result[m] = 'R'
        return ''.join(result)
