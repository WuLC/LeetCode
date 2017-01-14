/*
* @Author: WuLC
* @Date:   2017-01-14 22:06:30
* @Last Modified by:   WuLC
* @Last Modified time: 2017-01-14 22:07:25
*/


// binary search, set right pointer to the sqrt(Integer.max_value)
public class Solution 
{
    public int mySqrt(int x) 
    {
        if (x<0) return -1; // not legal
        int left = 0 , right = 46340, mid;
        while (left < right)
        {
            mid = left + ((right - left)>>1);
            if (mid*mid == x) return mid;
            else if(mid*mid > x) right = mid - 1;
            else left = mid+1;
        }
        if(left*left > x) return left-1;
        else return left;
    }
}