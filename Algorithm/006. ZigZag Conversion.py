#encoding:utf-8
##########################
#将给定的字符串表示成锯齿形，再逐行读出
##########################
class  Solution(object):
    def convert(self,s,numRows):
        """
        type s : str
        type numRows : int
        rtype : str
        """
        #不加下面判断时numRows=1时，interval为0，会导致死循环
        if numRows == 1:
            interval=numRows
        else:
            interval=(numRows-1)*2
        strLen=len(s)
        result=''
        for i in range(numRows):
            #第一行和最后一行
            if i==0 or i==(numRows-1):
                j=i
                while j<strLen :
                    result+=s[j]
                    j+=interval
            #其他行的情况，相邻的字符间的间隔大小为两个整数交替出现
            else:
                j=i
                flag=1
                firstInterval=(numRows-1-i)*2
                secondInterval=interval-firstInterval
                while j<strLen:
                    if flag==1:
                        result+=s[j]
                        j+=firstInterval
                        flag=2
                    elif flag==2:
                        result+=s[j]
                        j+=secondInterval
                        flag=1
        return result





