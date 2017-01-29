/**
* Author: WuLC
* Date:   2017-01-29 20:41:03
* Last modified by:   WuLC
* Last Modified time: 2017-01-29 20:41:26
* Email: liangchaowu5@gmail.com
*/


// two pointers
public class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        if(nums.length == 0) return 0;
        int p1 = 1, p2 = 1, count = 1;
        while(p2 < nums.length)
        {
            if(nums[p1-1] != nums[p2])
            {
                nums[p1] = nums[p2];
                p1++;
                count = 1;
            }
            else if (count < 2)
            {
                nums[p1] = nums[p2];
                p1++;
                count++;
            }
            p2++;

        }
        return p1;
    }
}