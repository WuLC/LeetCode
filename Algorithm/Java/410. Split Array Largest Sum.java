/**
* Author: WuLC
* Date:   2017-06-08 21:03:54
* Last modified by:   WuLC
* Last Modified time: 2017-06-08 21:05:17
* Email: liangchaowu5@gmail.com
*/



// binary search
// one important fact is : max(nums) <= largest sum <= sum(nums)
public class Solution 
{
    public int splitArray(int[] nums, int m) 
    {
        int maxNum = 0, sum = 0;
        for(int num : nums)
        {
            maxNum = Math.max(maxNum, num);
            sum += num;
        }
        
        // binary search 
        int left = maxNum, right = sum, mid;
        while (left < right)
        {
            int tmpSum = 0, count = 1;
            mid = left + ((right - left) >> 1);
            for(int num : nums)
            {
                if (tmpSum + num <= mid) tmpSum += num;
                else
                {
                    count += 1;
                    tmpSum = num;
                }
            }
            if (count <= m) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}