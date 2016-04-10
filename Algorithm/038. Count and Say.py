# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-10 21:02:37
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-10 21:05:53
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s = '1'
        for i in range(n-1):
            char = ''
            count = 0
            tmp = ''
            for j in range(len(s)):
                if char == s[j]:
                    count += 1
                    if j == len(s)-1:   # the last chatacter
                        tmp += (str(count)+char) 
                else:
                    if count>0:
                        tmp += (str(count)+char) 
                    if j == len(s)-1:  # the last character
                        tmp += ('1'+s[j])
                    char = s[j]
                    count = 1
            s = tmp
        return s
        