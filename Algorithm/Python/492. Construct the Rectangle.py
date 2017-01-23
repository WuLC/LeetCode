# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-01-24 00:02:10
# @Last modified by:   WuLC
# @Last Modified time: 2017-01-24 00:02:23
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in reversed(xrange(1, int(math.sqrt(area))+1)):
            if area%i == 0:
                return [area/i, i]
        