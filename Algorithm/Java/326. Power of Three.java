/*
* @Author: WuLC
* @Date:   2017-07-05 10:41:26
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-05 10:45:43
* @Email: liangchaowu5@gmail.com
*/


// 1162261467 = 3^19 since 3^20 is larger than the largest integer

public class Solution 
{
    public boolean isPowerOfThree(int n) 
    {
        return n > 0 && (1162261467 % n == 0);
    }
}