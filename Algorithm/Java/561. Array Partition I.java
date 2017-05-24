/**
* Author: WuLC
* Date:   2017-05-24 09:51:53
* Last modified by:   WuLC
* Last Modified time: 2017-05-24 09:53:24
* Email: liangchaowu5@gmail.com
*/


// sort and sum up the numbers of even index(start from 0)
public class Solution 
{
    public int arrayPairSum(int[] nums)
    {
        Arrays.sort(nums);
        int idx = 0, result = 0;
        while (idx < nums.length)
        {
            result += nums[idx];
            idx += 2;
        }
        return result;
    }
}