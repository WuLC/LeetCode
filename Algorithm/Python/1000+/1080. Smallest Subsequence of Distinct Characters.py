# -*- coding: utf-8 -*-
# Created on Sun Jun 09 2019 18:26:4
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# stack
from collections import Counter, defaultdict
class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        count = Counter(text)
        stack = []
        in_stack = defaultdict(bool)
        for c in text:
            if in_stack[c]:
                count[c] -= 1
                continue
            while stack and ord(stack[-1]) > ord(c) and count[stack[-1]] > 1:
                count[stack[-1]] -= 1
                in_stack[stack[-1]] = False
                stack.pop()
            stack.append(c)
            in_stack[c] = True
        return ''.join(stack)
            