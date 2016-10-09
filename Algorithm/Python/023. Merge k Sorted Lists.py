# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-27 12:43:15
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:52
# @Email: liangchaowu5@gmail.com


# 方法一：线性合并，时间复杂度为n^2
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return None
        
        mergedList = lists[0]
        for i in range(1,k):
            mergedList = self.mergeTwoLists(mergedList,lists[i])
        return mergedList
            
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(0)
        nextNode = dummy
        while l1 and l2:
            if l1.val > l2.val:
                nextNode.next = l2
                nextNode = nextNode.next
                l2 = l2.next
            else:
                nextNode.next = l1
                nextNode = nextNode.next
                l1 = l1.next
        
        if l1:
            nextNode.next = l1
            
        if l2:
            nextNode.next = l2
        
        return dummy.next

        
# http://blog.csdn.net/linhuanmars/article/details/19899259
# 方法二：类似与归并排序的合并,能够AC。run time: 164 ms
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return None
        return self.helper(lists,0,len(lists)-1)


    def helper(self,lists,l,r):
        if l<r:
            m = (r-l)/2
            return self.mergeTwoLists(self.helper(lists,l,l+m),self.helper(lists,l+m+1,r))
        else:
            return lists[l]
        
    def mergeTwoLists(self,l1,l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next
               


# 方法三：利用含有k个点的heap，每次找出最小的点. 284 ms
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0:
            return None

        listsHeap = []
        listsHeap.append(0) # 使堆中的元素从1开始
    
        for i in range(k):
            if lists[i] == None: # avoid empty list
                continue
            listsHeap.append(lists[i])
        
        dummy = ListNode(0)
        curr = dummy
        
        # 初始化堆有两种方法
        '''方法一
        j = len(listsHeap) - 1 
        while j > 1:
            if listsHeap[j].val<listsHeap[j/2].val:
                listsHeap[j],listsHeap[j/2] = listsHeap[j/2],listsHeap[j]
                self.siftDown(listsHeap,j)  #必须，否则初始建的堆会有问题
            j-=1
        '''
        # 方法二
        leafParent = (len(listsHeap)-1)/2
        for i in range(leafParent,0,-1):
            siftDown(listsHeap,i)
        while len(listsHeap) > 1:
            curr.next = listsHeap[1]
            curr = curr.next
            if listsHeap[1].next == None:  # 将空的列表移到最后并删除
                listsHeap[1] = listsHeap[len(listsHeap)-1] 
                del(listsHeap[len(listsHeap)-1])
            else:
                listsHeap[1] = listsHeap[1].next
            self.siftDown(listsHeap,1)

        return dummy.next


    def siftDown(self,listsHeap,i):
        while i*2+1 <= len(listsHeap):
            if i*2+1 < len(listsHeap):
                if listsHeap[i].val > min(listsHeap[i*2].val,listsHeap[i*2+1].val):
                    if listsHeap[i*2].val < listsHeap[i*2+1].val:
                        listsHeap[i],listsHeap[i*2] = listsHeap[i*2],listsHeap[i]
                        i = i*2
                    else:
                        listsHeap[i],listsHeap[i*2+1] = listsHeap[i*2+1],listsHeap[i]
                        i = i*2+1
                else:
                    return 
            elif i*2+1 == len(listsHeap):
                if listsHeap[i*2].val < listsHeap[i].val:
                    listsHeap[i],listsHeap[i*2] = listsHeap[i*2],listsHeap[i]
                i = i*2 
        return