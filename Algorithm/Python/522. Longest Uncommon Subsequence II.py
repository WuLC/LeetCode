# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-04 21:54:50
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-21 16:26:45
# @Email: liangchaowu5@gmail.com


# only those strings that appear just once can possibly be the Longest Uncommon Subsequence
# judge if those strings that appear just once are subsequence of other strings, if not update the result with its length
# time complexity: O(kn^2), k is the average length of strs and n is the length of strs
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_length = max(map(lambda x:len(x), strs))
        count = {}
        for s in strs:
            count.setdefault(s, 0)
            count[s] += 1
        result = -1
        for k,v in count.items():
            if v==1:
                if len(k) == max_length:
                    return max_length
                elif not self.isSubsequence(k, strs):
                    result = max(result, len(k))
        return result
                    


    def isSubsequence(self, s1, strs):
        for s2 in strs:
            if s1 == s2:
                continue
            p1, p2 = 0, 0
            while p1 < len(s1) and p2 < len(s2):
                if s1[p1] == s2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
            if p1 == len(s1):
                return True
        return False
        
        
            