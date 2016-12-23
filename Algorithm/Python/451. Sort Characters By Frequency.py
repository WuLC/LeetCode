# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-23 16:43:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-23 17:03:35
# @Email: liangchaowu5@gmail.com


# sort the hashmap
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        count = {}
        for char in s:
            count.setdefault(char, 0)
            count[char] += 1
        sorted_dict = sorted(count.items(), key = lambda x:x[1], reverse = True)
        for pair in sorted_dict:
            result += pair[0]*pair[1]
        return result