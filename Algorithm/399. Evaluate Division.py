# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-21 19:34:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-21 19:42:10
# @Email: liangchaowu5@gmail.com


# DFS
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mapping = collections.defaultdict(dict)
        for i in xrange(len(equations)):
            f, t = equations[i][0], equations[i][1]
            mapping[f][t] = values[i]
            if values[i]:
                mapping[t][f] = 1/values[i]
            else:
                mapping[t][f] = -1.0
        result = []
        for que in queries:
            result.append(self.dfs(mapping, que[0], que[1], set()))
        return result
            

    def dfs(self, mapping, s, e, visited):
        """return result of s/e"""
        if s not in mapping:
            return -1.0
        if s == e:
            return 1.0
        candidates = mapping[s]
        visited.add(s) # avoid endless loop
        for k in candidates.keys():
            if k == e:
                return candidates[k]
            if k not in visited:
                tmp = self.dfs(mapping, k, e, visited)
                if tmp != -1.0 and candidates[k] != -1.0:
                    return tmp * candidates[k]
        visited.remove(s)
        return -1.0
        
            
            
        
        
            