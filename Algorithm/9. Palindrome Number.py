#encoding:utf-8

#将数字转换为字符串再判断是否为回文

class Solution(object):
    def isPalindrome(self,x):
        """
        type x : int
        rtype :bool
        """
        strX=str(x)
        strLen=len(strX)
        flag=True
        for i in range(strLen/2):
            if strX[i] != strX[strLen-1-i]:
                flag=False
                return flag
        return flag