# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-13 10:07:57
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-13 10:23:43



class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]
        for m in moves:
            if m == 'U':
                pos[1] += 1
            elif m == 'D':
                pos[1] -= 1
            elif m == 'L':
                pos[0] -= 1
            elif m == 'R':
                pos[0] += 1
        return pos[0] == 0 and pos[1] == 0