class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647  
        if divisor == 0:
            return MAX_INT
    
        flag = 1
        if (dividend > 0 and divisor<0 ) or (dividend<0 and divisor >0):
            flag = -1
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        while a >= b :
            sum = b
            count =1 
            while a >= sum+sum:
                sum += sum
                count += count
            a-=sum
            res+=count

        # 溢出情况  
        if res*flag > pow(2,31)-1:
            return MAX_INT
        else:
            return res*flag