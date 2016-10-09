# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 18:28:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 18:28:32
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count, result= {}, []
        for i in xrange(len(s)-9):
            tmp = s[i:i+10]
            if tmp not in count:
                count[tmp] = 0
            count[tmp] += 1
            
        for k,v in count.items():
            if count[k] > 1:
                result.append(k)
        return result