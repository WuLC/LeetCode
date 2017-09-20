# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-20 14:15:53
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-20 14:28:09


# stack
# use stack to store indices of left brace and star
# pop left brace whenever meeting right brace, when left brace is empty, pop stars
# finally check whether left brace if empty, else use stars to map with them
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_idx, star_idx = [], []
        for i in xrange(len(s)):
            if s[i] == '(':
                left_idx.append(i)
            elif s[i] == '*':
                star_idx.append(i)
            else:
                if left_idx:
                    left_idx.pop()
                elif star_idx:
                    star_idx.pop()
                else:
                    return False
        while left_idx and star_idx:
            if left_idx[-1] > star_idx[-1]:
                break
            else:
                left_idx.pop()
                star_idx.pop()
        return len(left_idx) == 0
            
        
        