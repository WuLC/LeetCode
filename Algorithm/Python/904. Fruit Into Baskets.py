# -*- coding: utf-8 -*-
# Created on Wed Sep 19 2018 15:42:5
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# Two pointers
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left, right = 0, 0
        counter = {}
        result = 0
        while right < len(tree):
            if tree[right] not in counter:
                result = max(result, right - left)
                while len(counter)==2:
                    counter[tree[left]] -= 1
                    if counter[tree[left]]==0:
                        del counter[tree[left]]
                    else:
                        left += 1
                counter[tree[right]] = 1
            else:
                counter[tree[right]] += 1
            right += 1
        result = max(result, right - left)
        return result