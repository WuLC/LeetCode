/**
* Author: WuLC
* Date:   2016-12-20 07:49:35
* Last modified by:   WuLC
* Last Modified time: 2016-12-20 07:56:37
* Email: liangchaowu5@gmail.com
*/


//similar to binary search, pay attention that n may be negative
public class Solution 
{
    public double myPow(double x, int n) 
    {
        if (n==0)  return (double)1;
        int flag = 1;
        if (n<0) 
        {
            n = -n;
            flag = -1;
        }
        int count = 1, maxCount = (n>>1);
        double result = x;
        while(maxCount >= count) // do not use n > count*2, since count*2 may be get overflow
        {
            result *= result;
            count <<= 1;
        }
        if (flag == 1) return result * myPow(x, n-count);
        else return 1/(result * myPow(x, n-count));
    }
}