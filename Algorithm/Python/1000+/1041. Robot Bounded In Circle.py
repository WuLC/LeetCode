# -*- coding: utf-8 -*-
# Created on Thu May 30 2019 9:42:53
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        trans = {(0, 1) : {"L":(-1, 0), "R":(1, 0)}, 
                 (0, -1): {"L":(1, 0), "R":(-1, 0)},
                 (-1, 0): {"L":(0, -1), "R":(0, 1)},
                 (1, 0): {"L":(0, 1), "R":(0, -1)}}
        r, c = 0, 0
        dr, dc = 0, 1
        for char in instructions*4:
            if char == "G":
                r += dr
                c += dc
            else:
                dr, dc = trans[(dr, dc)][char]
        return r == 0 and c == 0
            
            
        
                        