#########################################
#方法一：同时遍历两个数组合并成一个
#时间复杂度O(m+n),居然AC了
#########################################

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index1=0
        index2=0
        mergedArr=[]
        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1] > nums2[index2]:
                mergedArr.append(nums2[index2])
                index2+=1
            elif nums1[index1] < nums2[index2]:
                mergedArr.append(nums1[index1])
                index1+=1
            else: #equal
                mergedArr.append(nums1[index1])
                mergedArr.append(nums2[index2])
                index1+=1
                index2+=1
            
        if index1!=len(nums1):
            while index1<len(nums1):
                mergedArr.append(nums1[index1])
                index1+=1
        
        if index2!=len(nums2):
            while index2<len(nums2):
                mergedArr.append(nums2[index2])
                index2+=1
        
        mergedLen=len(mergedArr)
        if mergedLen %2 == 0: #even length
            return float(mergedArr[mergedLen/2]+mergedArr[mergedLen/2-1])/2 
        else:                 #odd length
            return float(mergedArr[(mergedLen-1)/2])
            
#########################################
# 方法二：对两个数组采用二分查找
# 时间复杂度O(log(m+n))
#########################################    
class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n / 2 + 1)
        else:
            smaller = self.findKth(A, B, n / 2)
            bigger = self.findKth(A, B, n / 2 + 1)
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A[k / 2:], B[0:k/2+1], k - k / 2)
        return self.findKth(A[0:k/2+1], B[k / 2:], k - k / 2)