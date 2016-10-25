/**
* Author: WuLC
* Date:   2016-10-25 16:01:12
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 16:13:01
* Email: liangchaowu5@gmail.com
*/


// sort and the use two pointers
// time complexity O(n^2)
public class Solution 
{
    public int threeSumClosest(int[] nums, int target) 
    {
        Arrays.sort(nums);
        Integer result = null, closest = null;
        int left, right, sum;
        for (int i=0; i<nums.length-2; i++)
        {
            left = i+1; 
            right= nums.length - 1; 
            sum = target - nums[i];
            closest = null;
            while (left < right)
            {
                int tmp = nums[left] + nums[right];
                if (tmp == sum) return target;
                else if(tmp > sum) right--;
                else left++;
                
                //update closest
                if (closest == null || Math.abs(closest-sum) > Math.abs(tmp-sum))
                    closest = tmp;
            }
        // update result
        if (result == null || Math.abs(closest+nums[i]-target) < Math.abs(result-target))
            result = closest+nums[i];
        }
        return result;
    }
    
}



// make the above code faster and more concise
public class Solution 
{
    public int threeSumClosest(int[] nums, int target) 
    {
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        int left, right, sum;
        for (int i=0; i<nums.length-2; i++)
        {
            left = i+1; 
            right= nums.length - 1; 
            while (left < right)
            {
                sum = nums[i] + nums[left] + nums[right];
                if (target == sum) return target;
                else if(target < sum) right--;
                else left++;
                
                if (Math.abs(result-target) > Math.abs(sum-target))
                    result = sum;
            }
        }
        return result;
    }
}