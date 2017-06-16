# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-16 10:49:28
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-16 10:52:34
# @Email: liangchaowu5@gmail.com

# find all the zones of the words in dictionary
# then sort the zones and merge the neighbor zones
# add blod tag to the merged zones of s
class Solution(object):
    def addBoldTag(self, s, dictionary):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        indices = {}
        for i in xrange(len(s)):
            indices.setdefault(s[i], [])
            indices[s[i]].append(i)
            
        zones = []
        for w in dictionary:
            if w[0] in indices:
                for index in indices[w[0]]:
                    if w == s[index: index+len(w)]:
                        zones.append([index, index + len(w) - 1])
        
        # no substring of s exist in dict
        if len(zones) == 0:
            return s
        
        # merge neighbor substring
        zones.sort(key = lambda x:x[0])
        boldArea = []
        start, end = zones[0][0], zones[0][1]
        for i in xrange(1, len(zones)):
            if zones[i][0] > end + 1:
                boldArea.append([start, end])
                start, end = zones[i]
            else:
                end = max(end, zones[i][1])
        boldArea.append([start, end])
                
        # generate result
        curr, result = 0, ''
        for area in boldArea:
            result += s[curr:area[0]]
            result += '<b>' + s[area[0]: area[1]+1] + '</b>'
            curr = area[1]+1    
        if curr != len(s):
            result += s[curr:]
        return result