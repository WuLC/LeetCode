# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 17:54:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 17:54:11
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index, t_index = self.count_index(s), self.count_index(t)
        if len(s_index) != len(t_index):
            return False
        for i in xrange(len(s_index)):
            if s_index[i] != t_index[i]:
                return False
        return True
        
    def count_index(self, s):
        char, index, count = {}, [], 0
        for i in xrange(len(s)):
            if s[i] not in char:
                char[s[i]] = count
                count += 1
                index.append([])
            index[char[s[i]]].append(i)
        return index    