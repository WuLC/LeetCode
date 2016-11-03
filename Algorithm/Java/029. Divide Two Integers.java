/**
* Author: WuLC
* Date:   2016-11-03 16:35:38
* Last modified by:   WuLC
* Last Modified time: 2016-11-03 17:31:11
* Email: liangchaowu5@gmail.com
*/

// similar to binary search, without using long type number
// change all number to negative since abs(Integer.MAX_VALUE) < abs(Integer.MIN_VALUE)
// use tmp >= (Integer.MIN_VALUE>>1) instead of tmp + tmp >= Integer.MIN_VALUE, since tmp + tmp may lead to overflow

public class Solution 
{
    public int divide(int dividend, int divisor) 
    {
        if (divisor == 0 || dividend==Integer.MIN_VALUE && divisor==-1) return Integer.MAX_VALUE;
        if (dividend ==0) return 0;
        int flag = 1;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0) ) flag = -1;
        if (dividend > 0) dividend = -dividend;
        if (divisor > 0) divisor = -divisor;
        
        int count, tmp, result = 0;
        while (dividend <= divisor)
        {
            count = 1;
            tmp = divisor;
            while (tmp >= (Integer.MIN_VALUE>>1) && dividend <= tmp + tmp)
            {
                tmp += tmp;
                count += count;
            }
            result += count;
            dividend -= tmp;
        }
        if (flag==-1) return -result;
        else return result;
    }
}