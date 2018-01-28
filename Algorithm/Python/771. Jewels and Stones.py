# -*- coding: utf-8 -*-
# Created on Sun Jan 28 2018 11:14:3
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# easy solution
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        count = 0
        for c in S:
            if c in jewels:
                count += 1
        return count