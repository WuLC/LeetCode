# encoding:utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路一：遍历一遍求出所有节点的数目，找出该删除的节点的位置
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nextNode = head.next
        num = 1
        while not nextNode == None:
            num +=1
            nextNode = nextNode.next
        
        delete = num-n+1
        if delete == 1:
            return head.next
            
        else:
            currNode = head
            i = 1
            while i<delete-1:
                currNode = currNode.next
                i+=1    
            currNode.next = currNode.next.next
        return head
        
# 思路二：链表反转，从后往前求第n个数,但是不符合题意，因为题目要求返回的链表其他元素顺序不变
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        preNode  = head
        nextNode = head.next
        tmp = None
        while not nextNode == None:
            preNode.next = tmp
            tmp = preNode
            preNode = nextNode
            nextNode = nextNode.next
        preNode.next = tmp
        head = preNode
        if n==1:
            return head.next
        else:    
            i = 1
            while i < n-1:
                nextNode = nextNode.next
                i += 1
            nextNode.next = nextNode.next.next
            return head

#思路三：只遍历一次
# 有问题的代码，没考虑到头元素被删除的情况
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        p1=head
        i = 1
        while i<=n:
            p1 = p1.next
            i += 1
        p2 = head
        while not p1.next==None:
            p1 = p1.next
            p2 = p2.next
        p2.next =p2.next.next
        return head
参考代码
class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0) 
        dummy.next=head
        p1=p2=dummy
        for i in range(n): 
            p1=p1.next
        while p1.next:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return dummy.next