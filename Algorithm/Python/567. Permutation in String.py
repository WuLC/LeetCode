# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-01 10:26:43
# @Last Modified by:   WuLC
# @Last Modified time: 2017-05-01 10:27:47


# two pointers
from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = defaultdict(int)
        for char in s1:
            count[char] += 1
        p1, p2, sub_str = 0, 0, defaultdict(int)
        while p2 < len(s2):
            if s2[p2] not in count:
                sub_str = defaultdict(int)
                p1 = p2 + 1
            else:
                sub_str[s2[p2]] += 1
                while sub_str[s2[p2]] > count[s2[p2]]:
                    sub_str[s2[p1]] -= 1
                    p1 += 1
                if p2 - p1 + 1 == len(s1):
                    return True
            p2 += 1
        return False