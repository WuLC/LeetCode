# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-01 13:53:29
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:23:08
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0: 
            return -1
            
        hlen = len(haystack)
        nlen = len(needle)
        for i in range(hlen-nlen+1):
            if haystack[i:i+nlen] == needle:
                return i
        return -1
            
            
            
            
            