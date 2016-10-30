/**
* Author: WuLC
* Date:   2016-10-30 20:30:25
* Last modified by:   WuLC
* Last Modified time: 2016-10-30 20:33:15
* Email: liangchaowu5@gmail.com
*/

// two pointers
// one for the end of the unrepeated sorted array, the other for the current index of the array
public class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        if (nums.length <= 1) return nums.length;
        int idx1 = 0, idx2 = 1;
        while (idx2 < nums.length)
        {
            if (nums[idx2] != nums[idx1]) 
            {
                idx1++; 
                nums[idx1] = nums[idx2];
            }
            idx2++;
        }
        return idx1 + 1;
    }
}