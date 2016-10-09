# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-11 22:13:03
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-11 22:35:19
# @Email: liangchaowu5@gmail.com



# use stack
# AC
class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


# error for some cases
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.curr = nestedList
        self.idx = 0
        self.stack = []

    def next(self):
        """
        :rtype: int
        """
        if self.idx == len(self.curr):
            if self.stack:
                self.curr, self.idx = self.stack.pop(), 0
            else:
                return 
        while (self.curr[self.idx].getInteger() or self.curr[self.idx].getList()) and not self.curr[self.idx].isInteger():
            tmp = self.curr[self.idx].getList()
            if self.idx+1 != len(self.curr):
                self.stack.append(self.curr[self.idx+1:])
            self.curr, self.idx = tmp, 0
        if self.curr[self.idx].getInteger() or self.curr[self.idx].getList():
            next_val = self.curr[self.idx].getInteger()
            self.idx += 1
            return next_val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx != len(self.curr) and (self.curr[self.idx].getInteger() or self.curr[self.idx].getList()) or self.stack
        