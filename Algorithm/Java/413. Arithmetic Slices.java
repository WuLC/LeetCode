/*
* @Author: WuLC
* @Date:   2017-06-15 16:59:15
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-15 17:01:55
* @Email: liangchaowu5@gmail.com
*/

// O(n) time, O(1) space
// find the longest arithmetic slice each time, then calculate all possible sub slices within this slice
public class Solution 
{
    public int numberOfArithmeticSlices(int[] A) 
    {
        int start = 0 , end = 1, result = 0;
        while (end < A.length - 1)
        {
            if (A[end+1] - A[end] == A[end] - A[end-1]) end++;
            else
            {
                if(end - start >= 2) result += ((end - start)*(end - start - 1)>>1);
                start = end;
                end++;
            }
        }
        if (end == A.length - 1 && end - start >= 2) result += ((end - start)*(end - start - 1)>>1);
        return result;
    }
}