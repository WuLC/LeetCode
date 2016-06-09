# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-09 13:29:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-09 15:23:37
# @Email: liangchaowu5@gmail.com


# method 1, hash table and sort
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count,result = {}, []
        for i in xrange(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
        tmp = sorted(count.items(), key=lambda x:x[1], reverse=True)
        for j in xrange(k):
            result.append(tmp[j][0])
        return result

# method 2, hash table and heap
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count,result = {}, []
        for i in xrange(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
        heap = list(count.items())
        # build heap
        for i in reversed(xrange(len(heap)/2)):
            self.sift_down(i, heap)
        while True:
            result.append(heap[0][0])
            if len(result) == k:
                return result
            heap[0] = heap.pop()
            self.sift_down(0, heap)
            
    def sift_down(self, i, heap):
        # sift down
        while i*2+1<len(heap):
            if i*2+2<len(heap) and heap[i*2+1][1] <= heap[i*2+2][1]:
                index = i*2+2
            else:
                index = i*2+1 
            if heap[index][1] > heap[i][1]:
                heap[index], heap[i] = heap[i], heap[index]
                i = index
            else:
                return
                
        
                
            
