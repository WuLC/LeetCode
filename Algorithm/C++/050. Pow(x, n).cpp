/*
 * Created on Sun Apr 29 2018 11:16:36
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// binary search
// be careful of the case when n = -2147483648, std::abs(n) =  -2147483648
// thus use long to avoid overflow
class Solution 
{
    public:
        double myPow(double x, int n) 
        {
            double result = 1, tmp;
            long m = n, count; // when n=-2147483648
            int flag = 1;
            if (n < 0) 
            {
                flag = -1;
                m *= -1;
            }; 
            while(m > 0)
            {
                count = 1;
                tmp = x;
                while(count <= m/2)
                {
                    tmp *= tmp;
                    count += count;
                }
                m -= count;
                result *= tmp;
            }
            if (flag == 1) return result;
            else return 1/result;
        }
};