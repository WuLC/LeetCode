/**
* Author: WuLC
* Date:   2016-12-09 18:38:27
* Last modified by:   WuLC
* Last Modified time: 2016-12-09 18:39:29
* Email: liangchaowu5@gmail.com
*/


// same idea with problem 41. First Missing Positive, move the current number to the correct position
public class Solution 
{
    public int missingNumber(int[] nums) 
    {
        for(int i=0; i< nums.length; i++)
        {
            while (nums[i] != i && nums[i] < nums.length && nums[nums[i]] != nums[i])
            {
                // swap nums[i] with nums[nums[i]]
                int tmp = nums[i];
                nums[i] = nums[nums[i]];
                nums[tmp] = tmp;
            }
        }
        for(int i=0;i<nums.length;i++)
        {
            if (nums[i]!=i) 
                return i;
        }
        return nums.length; // empty array or the missing number is n
    }
}