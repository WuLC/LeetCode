# -*- coding: utf-8 -*-
# Created on Fri Mar 16 2018 22:23:51
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# just check who can reach the target firstly
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tar_sum = abs(target[0]) + abs(target[1])
        for g in  ghosts:
            if abs(g[0]-target[0]) + abs(g[1]-target[1]) <= tar_sum:
                return False
        return True