/*
* @Author: WuLC
* @Date:   2017-08-09 15:54:53
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-09 15:55:19
* @Email: liangchaowu5@gmail.com
*/

// use long type instead of int
public class Solution
{
    public boolean isPerfectSquare(int num) 
    {
        long left = 1, right = num, mid, tmp;
        while (left <= right)
        {
            mid = left + ((right - left)>>1);
            tmp = mid * mid;
            if (tmp == num) return true;
            else if(tmp > num) right = mid - 1;
            else left = mid + 1;  
        }
        return false;
    }
}