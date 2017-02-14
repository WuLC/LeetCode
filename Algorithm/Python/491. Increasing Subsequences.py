# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-14 14:59:54
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-14 15:06:11
# @Email: liangchaowu5@gmail.com

# use set 
# list can not be hashed, so it can't be stored in set, but tuple can be hashed, the reason is that list is mutable but tuple isn't
# but tuple can be concatenated
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seqs = set()
        for num in nums:
            new_seqs = {(num,)}
            for seq in seqs:
                if seq[-1] <= num:
                    new_seqs.add(seq+(num,))
            seqs |= new_seqs
        return [seq for seq in seqs if len(seq) > 1]

# more concise version
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seqs = set()
        for num in nums:
            seqs |= { seq+(num,) for seq in seqs if seq[-1] <= num}
            seqs.add((num,))
        return [seq for seq in seqs if len(seq) > 1]
            