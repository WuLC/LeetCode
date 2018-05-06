# -*- coding: utf-8 -*-
# Created on Sun May 06 2018 12:33:25
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Simple solution
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            name1, name23 = S.split('@')
            name2, name3 = name23.split('.')
            name1 = name1[0].lower() + '*****' + name1[-1].lower()
            return name1 + '@' + name2.lower() + '.' + name3.lower()
        else:
            tmp = ''
            for c in S:
                if c.isdigit():
                    tmp += c
            if len(tmp) > 10:
                return '+{0}-{1}-{2}-{3}'.format((len(tmp) - 10) * '*', '***', '***', tmp[-4:])
            else:
                return '{0}-{1}-{2}'.format('***', '***', tmp[-4:])