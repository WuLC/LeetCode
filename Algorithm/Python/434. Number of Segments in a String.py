# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-07 19:00:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-07 19:00:59
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())