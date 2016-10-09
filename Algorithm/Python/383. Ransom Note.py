# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-17 13:59:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-17 13:59:18
# @Email: liangchaowu5@gmail.com
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for s in magazine:
            count.setdefault(s, 0)
            count[s] += 1
        for s in ransomNote:
            if s in count and count[s] != 0:
                count[s] -= 1
            else:
                return False
        return True