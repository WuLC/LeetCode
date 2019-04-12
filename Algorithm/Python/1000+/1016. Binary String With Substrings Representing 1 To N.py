# -*- coding: utf-8 -*-
# Created on Fri Apr 12 2019 22:10:20
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# set
class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        result = {0}
        curr, nex = {0}, {0}
        for c in S:
            bit = int(c)
            curr, nex = nex, {0}
            for num in curr:
                val = (num << 1) + bit
                if val <= N:
                    result.add(val)
                    nex.add(val)
            if len(result) == N + 1:
                print(result)
                return True
        return False
        