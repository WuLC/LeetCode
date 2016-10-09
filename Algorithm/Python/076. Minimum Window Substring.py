# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-15 16:21:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-15 16:24:59
# @Email: liangchaowu5@gmail.com

# two pointers, with a dictionary and counter to determine whether the current substring contains t
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for c in s:
            dic[c] = 0
        for c in t:
            if c not in dic:
                return ""
            dic[c] += 1
        counter = len(t)
        start, end=0, 0
        INT_MAX = pow(2,31)-1
        min_start, min_len = 0, INT_MAX
        while end < len(s):
            if dic[s[end]] > 0:
                counter -= 1
            dic[s[end]] -= 1
            end += 1
            while counter==0:
                tmp = end - start 
                if min_len > tmp:
                    min_len = tmp
                    min_start = start
                dic[s[start]] += 1
                if dic[s[start]] > 0:
                    counter += 1
                start += 1
        if min_len != INT_MAX:
            return s[min_start:min_start+min_len]
        else:
            return ""
                    
        