/**
* Author: WuLC
* Date:   2016-11-30 17:57:07
* Last modified by:   WuLC
* Last Modified time: 2016-11-30 18:00:24
* Email: liangchaowu5@gmail.com
*/


// binary search, O(log(n))
// after selecting middle number, either part on its left or right will be in order
public class Solution 
{
    public int search(int[] nums, int target) 
    {
        int left = 0, right = nums.length-1, mid;
        while (left <= right)
        {
            mid = left + ((right - left)>>1);
            if (nums[mid] == target) return mid;
            if (nums[mid] >= nums[left]) // left is in order, add = to deal with case like [3, 1]
            {
                if (target >= nums[left] && target < nums[mid]) right = mid - 1;
                else left = mid + 1;
            }
            else  // right part is in order
            {
                if (target > nums[mid] && target <= nums[right]) left = mid + 1;
                else right = mid - 1;
            }
        }
        return -1;
    }
}