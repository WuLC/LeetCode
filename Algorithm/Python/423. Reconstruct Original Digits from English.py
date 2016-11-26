# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-26 10:09:26
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-26 10:17:36
# @Email: liangchaowu5@gmail.com

# each even number has a unique character, find all even numbers with these unique characters first 
# then all numbers left are odd, since any odd number can not be formed by any other odd numbers, we can get them one by one
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapping = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        unique_map = {0:'z', 2:'w', 4:'u', 6:'x', 8:'g'}
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        nums = collections.defaultdict(int)
        # even number
        for k, v in unique_map.items():
            while count[v] != 0: # defaultdict need not to judge whether the key is in it or not
                nums[k] += 1
                for c in mapping[k]:
                    count[c] -= 1
        
        # odd number
        for i in xrange(1,10,2):
            while all([count[c]!=0 for c in mapping[i]]):
                nums[i] += 1
                for c in mapping[i]:
                    count[c] -= 1
        
        # get result
        result = ''
        for i in xrange(10):
            for j in xrange(nums[i]):
                result += str(i)
        return result