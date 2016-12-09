/**
* Author: LC
* Date:   2016-12-09 11:36:01
* Last modified by:   WuLC
* Last Modified time: 2016-12-09 11:41:46
* Email: liangchaowu5@gmail.com
*/


// the first missing positive number must be between [1, nums.length+1], so we can make use of the indices
// traverse the array, swap current number to the correct position if its values is between [1, nums.length]
// repeat the  moving process until the current number is in the correct position or cannot find a correct position for it
// then traverse the array, the first number that doesn't match nums[i] == i+1 is the first missing positive number
public class Solution 
{
    public int firstMissingPositive(int[] nums) 
    {
        for(int i=0; i < nums.length; i++)
        {
            while(nums[i] != i+1 && nums[i]>0 && nums[i] <= nums.length && nums[nums[i]-1] != nums[i])
            {
                //swap nums[i] and nums[nums[i]-1]
                int tmp = nums[i];
                nums[i] = nums[nums[i]-1];
                nums[tmp-1] = tmp;
            }
        }
        
        // find the first missing positive number
        for (int i=0; i<nums.length; i++)
        {
            if (nums[i] != i+1) return i+1;
        }
        return nums.length+1; // the array contains all positive numbers from 1 to nums.length
    }
}