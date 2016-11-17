# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-17 23:31:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-17 23:31:58
# @Email: liangchaowu5@gmail.com

# sort and two pointers
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        pg, ps, count = 0, 0, 0
        while pg < len(g) and ps < len(s):
            if g[pg] <= s[ps]:
                count += 1
                pg += 1
                ps += 1
            else:
                ps += 1
        return count    