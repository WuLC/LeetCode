/*
 * Created on Sun Apr 29 2018 10:16:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// binary 
// pay attention when int*int > MAX_INT, overflow occures; use long instead of int
class Solution 
{
    public:
        int mySqrt(int x) 
        {
            long left = 0, right = x, mid; // use long instead of int to avoid overflow
            while (left < right-1)
            {
                mid = (left + right)>>1;
                if (mid*mid > x) right = mid - 1;
                else left = mid;
            }
            if (right*right <= x) return right;
            else return left;
        }
};