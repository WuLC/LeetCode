# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-11 16:10:45
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-11 23:27:53
# @Email: liangchaowu5@gmail.com

# method 1, start from all possible starting nodes, TLE
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_nodes = []
        n = len(gas)
        for i in xrange(n):
            if gas[i] >= cost[i]:
                start_nodes.append(i)
        for node in start_nodes:
            if self.can_reach(node, n, gas, cost):
                return node
        return -1
    
    def can_reach(self, node, n, gas, cost):
        total = 0
        for i in xrange(n):
            node = node % n
            total += gas[node]
            if total >= cost[node]:
                total -= cost[node]
            else:
                return False
            node += 1
        return True

# method 2, two pointers
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, end = len(gas)-1, 0
        total = gas[start] - cost[start]
        while start > end:
            if total>=0:
                total += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                total += gas[start] - cost[start]
        return start if total >= 0 else -1
        
            
        