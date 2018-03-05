# -*- coding: utf-8 -*-
# Created on Tue Feb 06 2018 9:55:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary tree, recursive
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        elif (K&1) == 0: # right child
            return 1 if self.kthGrammar(N-1, (K+1)/2) == 0 else 0
        else: # left child
            return 0 if self.kthGrammar(N-1, (K+1)/2) == 0 else 1
            