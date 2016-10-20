/**
* Author: WuLC
* Date:   2016-10-17 22:45:00
* Last modified by:   WuLC
* Last Modified time: 2016-10-21 00:16:01
* Email: liangchaowu5@gmail.com
*/

// transfer the problem to finding the kth element of two sorted arrays, which should be the first k/2+1 numbers of both array
// time complexity(logk)    
public class Solution 
{
    private int nums1Left;
    private int nums1Right;
    private int nums2Left;
    private int nums2Right;
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) 
    {
        nums1Left = 0; nums1Right = nums1.length-1; nums2Left = 0; nums2Right = nums2.length-1;
        int length = nums1.length + nums2.length;
        if (length % 2 == 1)
        {
            return findKthNumber(nums1, nums2, length/2+1)*1.0;
        }
        else
        {
            int smaller = findKthNumber(nums1, nums2, length/2);
            // after finding the smaller, pointers has been changed
            nums1Left = 0; nums1Right = nums1.length-1; nums2Left = 0; nums2Right = nums2.length-1;
            int bigger = findKthNumber(nums1, nums2, length/2+1);
            return (smaller + bigger)/2.0;
        }
    }

    /*find the kth element of two sorted arrays*/
    public int findKthNumber(int[] nums1, int[] nums2, int k)
    {
        if (nums1Left > nums1Right)
            return nums2[nums2Left + k-1];
        if (nums2Left > nums2Right)
            return nums1[nums1Left + k-1];
        if (k == 1)
            return Math.min(nums1[nums1Left], nums2[nums2Left]);
            
        int n1=0, n2=0;
        int nums1Length = nums1Right - nums1Left + 1, nums2Length = nums2Right - nums2Left + 1;
        if (nums1Length >= k/2)  n1 = nums1[nums1Left + k/2 - 1];
        if (nums2Length >= k/2)  n2 = nums2[nums2Left + k/2 - 1];
        
        if (nums1Length  < k/2) nums2Left += k/2;
        else if (nums2Length < k/2)  nums1Left += k/2;
        else if (n1 > n2) 
        {
            nums2Left += k/2;  // remove the 
            if (nums1Left + k/2 <= nums1Right) nums1Right = nums1Left + k/2;
        }
        else 
        {
            nums1Left += k/2;
            if (nums2Left + k/2 <= nums2Right) nums2Right = nums2Left + k/2;
        }
        return findKthNumber(nums1, nums2, k - k/2);
    }
}