# -*- coding: utf-8 -*-
# Created on Tue Dec 18 2018 20:37:24
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap
from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = Counter(A)
        nums = sorted(count.keys())
        for num in nums:
            if count[num] == 0:
                continue
            if num < 0:
                if num % 2 != 0 or num/2 not in count or count[num/2] < count[num]:
                    return False
                else:
                    count[num/2] -= count[num]
                    count[num] = 0
            else:
                if num*2 not in count or count[num*2] < count[num]:
                    return False
                else:
                    count[num*2] -= count[num]
                    count[num] = 0
        return True