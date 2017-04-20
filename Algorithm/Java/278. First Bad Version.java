/**
* Author: WuLC
* Date:   2017-04-20 15:07:25
* Last modified by:   WuLC
* Last Modified time: 2017-04-20 15:07:48
* Email: liangchaowu5@gmail.com
*/

// binary search 
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl 
{
    public int firstBadVersion(int n) 
    {
        int left = 1, right = n, mid;
        while (left < right)
        {
            mid = left + ((right - left)>>1);
            if (isBadVersion(mid)) right = mid;
            else left = mid + 1;
        }
        if (isBadVersion(left)) return left;
        else return left + 1;
    }
}