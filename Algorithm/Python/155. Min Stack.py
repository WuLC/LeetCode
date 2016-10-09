# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-30 20:55:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-30 20:55:54
# @Email: liangchaowu5@gmail.com

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.mini == None or len(self.stack) == 0:
            self.stack.append(0)
            self.mini = x
        else:
            self.stack.append(x - self.mini)
            if x-self.mini < 0:
                self.mini = x
            

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0: return 
        gap = self.stack.pop()
        if gap < 0:
            self.mini -= gap
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return
        if self.stack[-1] > 0:
            return self.mini+self.stack[-1]
        else:
            return self.mini
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini