# -*- coding: utf-8 -*-
# Created on Thu Jun 07 2018 18:40:44
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# count and sort

from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False
        counter = Counter(hand)
        record = [[k, v] for k, v in sorted(counter.items())]
        idx = 0
        while idx <= len(record)-W:
            if record[idx][1] > 0:
                num, count = record[idx]
                record[idx][1] = 0
                for i in xrange(idx+1, idx+W):
                    if record[i][0] - record[i-1][0] != 1 or record[i][1] < count:
                        return False
                    record[i][1] -= count
            idx += 1
        return record[-1][1] == 0