/**
* Author: WuLC
* Date:   2017-05-04 15:07:29
* Last modified by:   WuLC
* Last Modified time: 2017-05-04 15:08:47
* Email: liangchaowu5@gmail.com
*/


// start testing from sqrt root of the area
public class Solution 
{
    public int[] constructRectangle(int area) 
    {
        for(int i = (int)Math.sqrt(area); i <= area; i++)
        {
            if( area % i == 0)
            {
                int j = area/i;
                return new int[]{Math.max(i, j), Math.min(i, j)};
            }
        }
        return new int[2];
    }
}