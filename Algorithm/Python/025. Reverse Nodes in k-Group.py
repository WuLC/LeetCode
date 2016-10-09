# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-03-30 20:09:39
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:56
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k<=1:
            return head
            
        current = head
        count = 0       # 记录是否第一次反转
        lastTail = None # 记录已反转元素的tail
        while not current == None:
            h1 = current
            flag = 0    # 标记剩余的nodes中是否有k个node
            for i in range(k-1):
                if not current == None:
                    current = current.next
                else:
                    flag = 1 #不足k个元素
            if current:
                current = current.next  #下一次待反转的head
            else:
                flag = 1  #防止current刚好为None，但是flag值不变
                
            if flag == 0:
                h,t = self.reverseList(h1,k)
                if count == 0:
                    head = h  #第一次反转后的head需要记下，用作返回值
                else:
                    lastTail.next = h # 连接上一次的tail与本次的head
                    
                lastTail = t
                lastTail.next = current
                count=1
                
            elif flag == 1 and count>0: # count=0时lastTail还是None,不能赋值
                lastTail.next = h1
        return head
                
    # 将长度为length的链表反转并返回反转后的头结点和尾节点    
    def reverseList(self,head,length):
        n1 = head
        n2 = n1.next
        tmp = n2.next
        while length >1:
            n2.next = n1
            n1 = n2
            n2 = tmp 
            if n2==None:
                return n1,head
            tmp =n2.next
            length-=1
        return n1,head