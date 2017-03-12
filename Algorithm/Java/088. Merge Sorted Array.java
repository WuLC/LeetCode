/**
* Author: WuLC
* Date:   2017-03-13 00:03:45
* Last modified by:   WuLC
* Last Modified time: 2017-03-13 00:04:26
* Email: liangchaowu5@gmail.com
*/

// two pointers, from large number to small number to ensure not to overlap
public class Solution 
{
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {
        int idx = m + n -1;
        int p1 = m-1, p2 = n-1;
        while (p1 >= 0 || p2 >= 0)
        {
            if (p1 >= 0 && (p2 < 0 || nums1[p1] > nums2[p2]))
            {
                nums1[idx--] = nums1[p1];
                p1--;
            }
            else
            {
                nums1[idx--] = nums2[p2];
                p2--;
            }
        }
    }
}