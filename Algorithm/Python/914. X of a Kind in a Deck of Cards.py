# -*- coding: utf-8 -*-
# Created on Tue Oct 02 2018 17:7:35
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Greatest Common Divisor
from collections import Counter
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x
        count = Counter(deck)
        return reduce(gcd, count.values())>1