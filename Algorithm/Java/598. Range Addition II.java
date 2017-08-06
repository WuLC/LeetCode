/*
* @Author: WuLC
* @Date:   2017-08-06 18:02:17
* @Last Modified by:   WuLC
* @Last Modified time: 2017-08-06 18:03:36
* @Email: liangchaowu5@gmail.com
*/


// find the minimum length and width
public class Solution 
{
    public int maxCount(int m, int n, int[][] ops) 
    {
        int len = m, width = n;
        for (int i = 0; i < ops.length; i++)
        {
            len = Math.min(len, ops[i][0]);
            width = Math.min(width, ops[i][1]);
        }
        return len * width;
    }
}