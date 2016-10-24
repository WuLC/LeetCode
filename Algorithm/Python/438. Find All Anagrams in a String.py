# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-24 22:14:58
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-24 22:15:52
# @Email: liangchaowu5@gmail.com


from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        s_len, p_len = len(s), len(p)
        if  s_len < p_len :
            return result
        tmp_chars, p_chars = defaultdict(int), defaultdict(int) # default value is 0
        for i in xrange(p_len):
            tmp_chars[s[i]] += 1
            p_chars[p[i]] += 1
        for i in xrange(s_len - p_len + 1):
            if i!= 0:
                tmp_chars[s[i+p_len-1]] += 1
            if tmp_chars==p_chars:
                result.append(i)
            tmp_chars[s[i]] -= 1
            if tmp_chars[s[i]] == 0:
                del tmp_chars[s[i]]
        return result
            
            