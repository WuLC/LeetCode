/**
* Author: LC
* Date:   2017-06-11 20:37:17
* Last modified by:   LC
* Last Modified time: 2017-06-11 20:42:12
* Email: liangchaowu5@gmail.com
*/


// bit manipulation
// (num&(-num)) == num is checking that num has only one bit that is not 0
// (num&0x55555555) == num is checking the only one bit that is not 0 is in the correct position
// avoid special case when num = 0
public class Solution 
{
    public boolean isPowerOfFour(int num) 
    {
        return  num != 0 && (num&(-num)) == num && (num&0x55555555) == num;
    }
}