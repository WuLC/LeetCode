/**
* Author: WuLC
* Date:   2016-12-09 18:38:27
* Last modified by:   WuLC
* Last Modified time: 2016-12-09 19:07:26
* Email: liangchaowu5@gmail.com
*/

// three methods
// 1. move the current number to correct place (2ms)
// 2. use sum from 1 to n to minus sum(nums)   (1ms)
// 3. bit manipulation                         (1ms)

// method 1
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


// method 2
// use sum from 1 to n to minus sum(nums)
public class Solution 
{
    public int missingNumber(int[] nums) 
    {
        int n = nums.length, sum=0;
        for(int i=0; i<nums.length; i++) sum+=nums[i];
        return (1+n)*n/2 - sum;
    }
}


// method 3, bit manipulation
public class Solution 
{
    public int missingNumber(int[] nums) 
    {
        int result = nums.length;
        for(int i=0; i<nums.length; i++)
        {
            result ^= i;
            result ^= nums[i];
        }
        return result;
    }
}