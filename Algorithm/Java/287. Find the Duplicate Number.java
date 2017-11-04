/*
 * Created on Sat Nov 04 2017 15:30:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// method 1, binary search 
// time O(nlogn), space O(1)
class Solution 
{
    public int findDuplicate(int[] nums) 
    {
        int left = 1, right = nums.length - 1;
        while(left < right)
        {
            int count = 0;
            int mid = left + ((right - left)>>1);
            for (int i = 0; i < nums.length; i++)
            {
                if(nums[i] <= mid)
                    count++;
            }
            if (count > mid) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}