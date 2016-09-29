# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-29 20:02:27
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-29 20:04:18
# @Email: liangchaowu5@gmail.com

# Stack, similar to the problem of removing k digits so that the remaining digits is smallest of largest
# the only difference if that it require the each character appear at least once, use a map to store it

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result, stored, count = [], set(), {}
        for char in s:
             count.setdefault(char, 0)
             count[char] += 1
        for char in s:
            if char in stored:
                count[char] -= 1
                continue
            else:
                while result and result[-1] > char and count[result[-1]] > 1:
                    count[result[-1]] -= 1
                    stored.remove(result.pop())
                stored.add(char)
                result.append(char)
        return ''.join(result[:len(set(s))])
        