# -*- coding: utf-8 -*-
# Created on Tue Oct 23 2018 16:34:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        idx1, idx2 = 0, 0
        n1, n2 = len(name), len(typed)
        while idx1 < n1 and idx2 < n2:
            if name[idx1] != typed[idx2]:
                return False
            cnt1, cnt2 = 0, 0 
            while idx1 + 1 < n1 and name[idx1 + 1] == name[idx1]:
                idx1 += 1
                cnt1 += 1
            while idx2 + 1 < n2 and typed[idx2 + 1] == typed[idx2]:
                idx2 += 1
                cnt2 += 1
            if cnt1 > cnt2:
                return False
            idx1 += 1
            idx2 += 1
        return True if idx1 == n1 and idx2 == n2 else False