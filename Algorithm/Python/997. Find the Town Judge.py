# -*- coding: utf-8 -*-
# Created on Mon Feb 25 2019 20:59:35
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# hashmap, simple solution
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        result, count = -1, {}
        for t in trust:
            if t[1] not in count:
                count[t[1]] = 0
            count[t[1]] += 1
            if count[t[1]] == N-1:
                if result < 0:
                    result = t[1]
                else:
                    return -1

        for t in trust:
            if t[0] == result:
                return -1
        return result