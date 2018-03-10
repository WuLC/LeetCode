# -*- coding: utf-8 -*-
# Created on Sat Mar 10 2018 11:7:38
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution
class Solution(object):
    def __init__(self):
        self.count = [0]
        
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if len(self.count) > N:
            return self.count[N]
        changedNums = {'2', '5', '6', '9'}
        unchangedNums = {'0', '1', '8'}
        for i in xrange(len(self.count), N+1):
            legal, changed = True, False
            for char in str(i):
                if char in unchangedNums:
                    continue
                elif char in changedNums:
                    changed = True
                else:
                    legal = False
                    break
            if legal and changed:
                self.count.append(self.count[-1]+1)
        return self.count[-1]
        
        