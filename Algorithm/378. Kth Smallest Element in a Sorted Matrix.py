# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-08 19:45:54
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-08 19:57:00
# @Email: liangchaowu5@gmail.com

# use heap, one node represents one line in the matrix, pop the minimal element each time 
# O(k*logn)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        heap = range(n)
        indices = [0 for i in xrange(n)]
        while k > 0:
            if k==1:
                return matrix[heap[0]][indices[heap[0]]]
            indices[heap[0]] += 1
            if indices[heap[0]] == n:
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()
                self.sift_down(matrix, heap, indices)
            else:
                self.sift_down(matrix, heap, indices)
            k -= 1
        
    def sift_down(self, matrix, heap, indices):
        i = 0
        while i < len(heap)/2:
            if i*2+2 < len(heap):
                tmp = min(matrix[heap[i*2+1]][indices[heap[i*2+1]]], matrix[heap[i*2+2]][indices[heap[i*2+2]]])
                idx = i*2+1 if tmp == matrix[heap[i*2+1]][indices[heap[i*2+1]]] else i*2+2
            else:
                tmp = matrix[heap[i*2+1]][indices[heap[i*2+1]]]
                idx = i*2+1
            if matrix[heap[i]][indices[heap[i]]] > tmp:
                heap[i], heap[idx] = heap[idx], heap[i]
                i = idx
            else:
                return
                
            
# heapq module in python can also implement this, and more concise and efficient
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        return list(heapq.merge(*matrix))[k-1]