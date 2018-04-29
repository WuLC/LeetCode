/*
 * Created on Sun Apr 29 2018 23:26:17
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bit manipulation
class Solution 
{
    public:
        int hammingDistance(int x, int y) 
        {
            int tmp = x^y, count = 0;
            while(tmp)
            {
                if(tmp&1) count++;
                tmp>>=1;
            }
            return count;
        }
};