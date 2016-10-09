# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 18:11:57
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 18:12:06
# @Email: liangchaowu5@gmail.com

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        count, n = 1, len(self.stack)
        while count < n:
            self.stack.append(self.stack[0])
            del self.stack[0]
            count += 1
        del self.stack[0]
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        