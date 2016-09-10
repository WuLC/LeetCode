# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-09 14:39:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-10 11:20:13
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: b
        """
        mapping, mapped = {}, set()
        words = str.split()
        if len(words) != len(pattern):
            return False
        for i in xrange(len(pattern)):
            if (pattern[i] in mapping and mapping[pattern[i]] != words[i]) or (pattern[i] not in mapping and words[i] in mapped):
                return False
            else:
                mapping[pattern[i]] = words[i]
                mapped.add(words[i])
        return True
                