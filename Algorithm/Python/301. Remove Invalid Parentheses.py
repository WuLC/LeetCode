# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-05 15:00:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-05 15:01:40
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        level = {s} # set
        while True:
            """
            for candidate in level:
                if self.is_valid(candidate):
                    result.append(candidate)
            """
            result = filter(self.is_valid, level) # the same as the above three lines
            if result:
                return result
            else:
                level = {can[:i]+can[i+1:] for can in level for i in xrange(len(can))}
                        

    def is_valid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count <= 0:
                    return False
                count -= 1
        return count == 0