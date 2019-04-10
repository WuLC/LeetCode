# -*- coding: utf-8 -*-
# Created on Tue Apr 09 2019 21:27:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy with two pointers

from collections import defaultdict

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        record = defaultdict(int)
        for s, e in clips:
            record[s] = max(record[s], e)
        sorted_clip = sorted(record.items())
        curr, nex, count = 0, 0, 0
        for c in sorted_clip:
            if curr >= T or nex < c[0]:
                break
            if curr < c[0]:
                count += 1
                curr = nex
            nex = max(nex, c[1])
        if curr >= T:
            return count
        elif nex >= T:
            return count + 1
        else:
            return -1
