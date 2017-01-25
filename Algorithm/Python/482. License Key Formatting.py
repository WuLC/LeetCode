# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-01-25 16:33:08
# @Last modified by:   WuLC
# @Last Modified time: 2017-01-25 16:33:37
# @Email: liangchaowu5@gmail.com


# string
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        idx, result = 0, []
        s = ''.join(S.split('-'))
        extra = len(s) % K
        if extra != 0:
            result.append(s[:extra].upper())
            idx = extra
        while idx < len(s):
            result.append(s[idx:idx+K].upper())
            idx += K
        return '-'.join(result)
        