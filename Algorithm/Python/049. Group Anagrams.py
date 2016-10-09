# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-30 11:43:12
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-30 11:50:56
# @Email: liangchaowu5@gmail.com


# method 1 ,TLE
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        result = []
        map_dict = []
        count = 0
        
        for i in xrange(n):
            flag = 0
            tmp = self.str2dict(strs[i])
            for i in xrange(len(map_dict)):
                if map_dict[i] == tmp:
                    result[i].append(strs[i])
                    flag = 1
            if flag == 0:
                map_dict.append(tmp)
                result.append([strs[i]])
        return result
            
    
    def str2dict(self,s):
        res = {}
        for i in s:
            if i not in res:
                res[i] = 0
            res[i] += 1
        return res
                
            
            
# method 2, AC
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {}
        strs.sort()
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in result_dict:
                result_dict[tmp] = []
            result_dict[tmp].append(s)
        
        return result_dict.values()