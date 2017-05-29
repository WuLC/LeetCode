/*
* @Author: WuLC
* @Date:   2017-05-29 22:57:31
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-29 22:58:24
* @Email: liangchaowu5@gmail.com
*/

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */


// binary search
public class Solution extends GuessGame 
{
    public int guessNumber(int n) 
    {
        int left = 1, right = n, mid;
        while (left < right)
        {
            mid = left + ((right - left) >> 1);
            int tmp = guess(mid);
            if ( tmp == 0 ) return mid;
            else if (tmp == 1) left = mid + 1 ;
            else right = mid - 1;
        }
        return left;
    }
}