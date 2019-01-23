# -*- coding: utf-8 -*-
# Created on Sun Jan 20 2019 10:59:15
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# two pointers, O(n) time
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 1
        left, right = 0, 1
        while right + 1 < len(A):
            if (A[right] > A[right-1] and A[right] > A[right+1]) or (A[right] < A[right-1] and A[right] < A[right+1]):
                right += 1
            else:
                if A[right] != A[right-1]:
                    result = max(result, right - left + 1)
                while right < len(A)-1 and A[right]==A[right+1]:
                    right += 1
                left, right = right, right + 1
        if right < len(A) and A[right] != A[right-1]:
            result = max(result, right - left + 1)
        return result
            

# O(n^2) time, two pointers, TLE
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = min(2, len(A))
        for i in xrange(1, len(A) - 1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                flag = 1
            elif A[i] < A[i-1] and A[i] < A[i+1]:
                flag = -1
            else:
                continue
            left, right = i - 1, i + 1
            tflag = flag
            while left - 1 >= 0:
                if tflag == 1 and A[left-1] > A[left]:
                    left -= 1
                    tflag *= -1
                elif tflag == -1 and A[left-1] < A[left]:
                    left -= 1
                    tflag *= -1
                else:
                    break
            tflag = flag
            while right + 1 < len(A):
                if tflag == 1 and A[right+1] > A[right]:
                    right += 1
                    tflag *= -1
                elif tflag == -1 and A[right+1] < A[right]:
                    right += 1
                    tflag *= -1
                else:
                    break         
            size = max(size, right - left + 1)
        return size