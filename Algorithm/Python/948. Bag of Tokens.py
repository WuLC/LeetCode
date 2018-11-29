# -*- coding: utf-8 -*-
# Created on Thu Nov 29 2018 20:19:8
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy
# trade small power for points, then trade points for large power, check the avaiable points after each trading
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        prefix_sum = []
        curr, result = 0, 0
        for t in tokens:
            curr += t
            prefix_sum.append(curr)
            if curr <= P:
                result += 1
        
        p1, p2 = 0, len(prefix_sum) - 1
        while p1 < p2:
            if P < tokens[p1]:
                break
            P += tokens[p2] - tokens[p1]
            p1 += 1
            p2 -= 1
            for i in xrange(p2, p1 - 1, -1):
                if prefix_sum[i] - prefix_sum[p1-1] <= P:
                    result = max(result, i - p1 + 1)
                    break
        return result