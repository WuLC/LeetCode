# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-17 00:24:43
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-17 00:25:25
# @Email: liangchaowu5@gmail.com


# simple counting
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA, countL = 0, 0
        idx, tmp = 0, 0
        while idx < len(s):
            if s[idx] != 'L':
                tmp = 0
            else:
                tmp += 1
                countL = max(tmp, countL)
            if s[idx] == 'A':
                countA += 1
            idx += 1
        return False if countA > 1 or countL > 2 else True