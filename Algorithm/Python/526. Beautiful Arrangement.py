# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-25 20:46:31
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-25 20:46:57
# @Email: liangchaowu5@gmail.com


# naive dfs, AC
class Solution(object):
    
    def __init__(self):
        self.used = set()
        self.result = 0
        
        
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.result = 0
        self.used = set()
        self.dfs(1, N)
        return self.result
        
        
    def dfs(self, idx, N):
        if idx == N+1:
            self.result += 1
            return 
        for num in xrange(1, N+1):
            if num not in self.used and (num%idx == 0 or idx%num == 0):
                self.used.add(num)
                self.dfs(idx+1, N)
                self.used.remove(num)
        