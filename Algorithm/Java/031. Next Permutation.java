/**
* Author: LC
* Date:   2016-11-27 13:23:52
* Last modified by:   WuLC
* Last Modified time: 2016-11-27 13:35:07
* Email: liangchaowu5@gmail.com
*/


// traverse the nums backwards, denote the current number as nums[i]
// stop when there exist a number with larger index and value compared to the nums[i]
// exchange nums[i] with the smallest number among those numbers with larger indices and values than nums[i]
// then sort the numbers with indices larger than i

public class Solution 
{
    public void nextPermutation(int[] nums)
    {
        int n = nums.length;
        int maxIndex = n-1;
        for (int i=n-2; i>=0; i--)
        {
            if(nums[maxIndex] > nums[i])
            {
                // find the smallest number that is greater than nums[i] after it 
                for (int j = i+1; j < n; j++)
                {
                    if (nums[j] > nums[i] && nums[j] < nums[maxIndex])
                        maxIndex = j;
                }
                int tmp = nums[i];
                nums[i] = nums[maxIndex];
                nums[maxIndex] = tmp;
                Arrays.sort(nums, i+1, n);
                return;
            }
            else maxIndex = i;
        }
        // rearrange it as the lowest possible order
        int tmp;
        for(int i=0; i<n/2; i++)
        {
            tmp = nums[i];
            nums[i] = nums[n-i-1];
            nums[n-i-1] = tmp;
        }
    }
}