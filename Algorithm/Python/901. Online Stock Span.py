# -*- coding: utf-8 -*-
# Created on Sat Sep 15 2018 19:58:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# stack
class StockSpanner(object):

    def __init__(self):
        self.nums = []
        self.stack = []
        self.idx = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while self.stack and self.nums[self.stack[-1]-1] <= price:
            self.stack.pop()
        self.nums.append(price)
        span = self.idx-self.stack[-1] if self.stack else self.idx
        self.stack.append(self.idx)
        self.idx += 1
        return span