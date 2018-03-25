# -*- coding: utf-8 -*-
# Created on Sun Mar 25 2018 11:7:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        count, curr = 0, 0
        for c in S:
            idx = ord(c) - 97
            if curr + widths[idx] > 100:
                count += 1
                curr = widths[idx]
            else:
                curr += widths[idx]
        return [count+1, curr]