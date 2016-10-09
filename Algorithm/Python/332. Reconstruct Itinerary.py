# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-27 14:14:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-27 16:08:34
# @Email: liangchaowu5@gmail.com

#######################################
# one ticket may appear several times
#######################################


# method 1, backtracking, TLE
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mapping, used = {}, {}
        for ticket in tickets:
            mapping.setdefault(ticket[0], [])
            mapping[ticket[0]].append(ticket[1])
            used.setdefault((ticket[0],ticket[1]), 0)
            used[(ticket[0],ticket[1])] += 1
        result = []
        self.helper('JFK', mapping, len(tickets)+1, ['JFK'], used, result)
        return result[0]
        
    
    def helper(self, start, mapping, n, tmp, used, result):
        if len(tmp) == n:
            if len(result)==0:
                result.append(tmp[:])
            elif self.smaller(tmp, result[0]):
                result[0] = tmp[:]
            return
        if start in mapping:
            for i in xrange(len(mapping[start])):
                if used[(start, mapping[start][i])] != 0:
                    used[(start, mapping[start][i])] -= 1
                    self.helper(mapping[start][i], mapping, n, tmp+[mapping[start][i]], used, result)
                    used[(start, mapping[start][i])] += 1
    
    def smaller(self, s1, s2):
        for i in xrange(len(s1)):
            if s1[i]<s2[i]:
                return True
            elif s1[i]>s2[i]:
                return False


# method 2,Greedy DFS, building the route backwards when retreating
# referer:https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        mapping = {}
        for start,end in tickets:
            mapping.setdefault(start, [])
            mapping[start].append(end)
        for k in mapping.keys():
            mapping[k].sort(reverse=True)
        route = []
        self.visit('JFK', mapping, route)
        return route[::-1]
    
    def visit(self, start, mapping, route):
        while start in mapping and mapping[start]:
            self.visit(mapping[start].pop(), mapping, route)
        route.append(start)