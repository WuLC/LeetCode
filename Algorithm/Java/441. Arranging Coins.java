/**
* Author: WuLC
* Date:   2016-11-02 12:00:45
* Last modified by:   WuLC
* Last Modified time: 2016-11-02 12:05:34
* Email: liangchaowu5@gmail.com
*/


// pay attention to overflow

public class Solution 
{
    public int arrangeCoins(int n) 
    {
        int left = 1, right=(int)(Math.sqrt(2) * Math.sqrt(n)), mid, total; 
        while(left <= right)
        {
            mid = left + ((right-left)>>1);
            // the following sum operation avoid overflow when (1+mid)*mid is operated
            if ((mid & 1) == 0) total = (1+mid)*(mid>>1);
            else total = ((1+mid)>>1)*mid;
            
            if (total == n) return mid;
            else if (total > n) right = mid - 1;
            else left = mid + 1;
        }
        return left-1;
    }
}