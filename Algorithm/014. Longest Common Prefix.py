# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-08 09:43:39
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:24
# @Email: liangchaowu5@gmail.com

# 功能：找出字符串

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) ==0:
            return ''
            
        prefix =''
        # 获取最短字符串的长度
        minLen = 1000000
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)       
        
        for i in range(minLen):
            equal = True
            char = strs[0][i]
            for s in strs:
                if not s[i] == char:
                    equal = False
                    break
            if equal:
                prefix += char
            else:
                break        
        return prefix
        
                
            
            
