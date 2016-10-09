/**
* Author: WuLC
* Date:   2016-10-09 20:14:25
* Last modified by:   WuLC
* Last Modified time: 2016-10-09 20:17:26
* Email: liangchaowu5@gmail.com
*/


// two pointers, O(n^2)
public class Solution 
{
    public List<List<Integer>> threeSum(int[] nums) 
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        int target, left, right, sum;
        for (int i=0; i<nums.length; i++)
        {   
            // avoid duplicate
            if (i>0 && nums[i] == nums[i-1]) 
                continue;
            target = -nums[i];
            left = i+1;
            right = nums.length -1;
            while (left < right)
            {   
                sum = nums[left] + nums[right];
                if (sum == target)
                {
                    result.add(new ArrayList(Arrays.asList(nums[i],nums[left],nums[right])));
                    left ++;
                    right --;
                    // avoid duplicate
                    while (left<right && nums[left] == nums[left-1])
                        left ++;
                }
                else if (sum > target) 
                    right --;
                else 
                    left ++;
            }
        }
        return result;
    }
}