# -*- coding: utf-8 -*-
# Created on Thu Aug 02 2018 21:8:33
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy, from small to large
# find the smllest number in A that is larger than the number in B

from collections import defaultdict
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        A = sorted(A)
        unused = []
        mapping = defaultdict(list)
        idx = 0
        for num in sorted(B):
            while idx<n and A[idx] <= num:
                unused.append(A[idx])
                idx += 1
            if idx == n:
                break
            mapping[num].append(A[idx])
            idx += 1
        result = [mapping[num].pop() if num in mapping and len(mapping[num])>0 else unused.pop() for num in B]
        return result
        

        
            


            
            
