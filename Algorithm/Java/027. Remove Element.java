/**
* Author: WuLC
* Date:   2016-10-30 20:34:42
* Last modified by:   WuLC
* Last Modified time: 2016-10-30 20:45:01
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    public int removeElement(int[] nums, int val) 
    {
        if (nums.length == 0) return 0;
        int left = 0, right = nums.length-1, tmp;
        while (left < right)
        {
            while (left < right && nums[left]!=val) left++;
            while (left < right && nums[right]==val) right--;
            if (left < right)
            {
                tmp = nums[left];
                nums[left++] = nums[right];
                nums[right--] = tmp;
            }
        }
        if (nums[left] != val) return left+1;
        else return left;
    }
}