# -*- coding: utf-8 -*-
# Created on Wed Jan 24 2018 21:21:45
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# find the longest intervel for each character and merge intersectional intervels
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        indices = {}
        for i in xrange(len(S)):
            if S[i] not in indices:
                indices[S[i]] = [i, i]
            else:
                indices[S[i]][1] = i
        blocks = sorted(indices.values(), key = lambda x:x[0])
        
        lens = []
        s, e = blocks[0]
        for i in range(1, len(blocks)):
            if blocks[i][0] > e:
                lens.append(e-s+1)
                s, e = blocks[i]
            elif blocks[i][1] > e:
                e = blocks[i][1]
        lens.append(e-s+1)
        return lens
                
        