# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-13 09:48:21
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-13 09:48:29
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c]<0: 
                return False 
        for k,v in count.items():
            if v != 0:
                return False
        return True