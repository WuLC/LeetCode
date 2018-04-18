/*
 * Created on Wed Apr 18 2018 9:26:4
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// no need to change int to str
// use long long to allow overflow case
class Solution 
{
    public:
        int reverse(int x) 
        {
            long long result = 0;
            while(x)
            {
                result = result*10 + x%10;
                x /= 10;
            }
            return (result > INT_MAX || result < INT_MIN) ? 0 : result;
        }
};