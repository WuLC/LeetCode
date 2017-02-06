/**
* Author: WuLC
* Date:   2017-02-06 17:09:03
* Last modified by:   WuLC
* Last Modified time: 2017-02-06 17:10:33
* Email: liangchaowu5@gmail.com
*/

// swap the array  to achieve nums[i]=i+1
public class Solution 
{
    public List<Integer> findDisappearedNumbers(int[] nums) 
    {
        List<Integer> result = new ArrayList<Integer>();
        for(int i=0; i< nums.length; i++)
        {
            while (nums[i] != i+1 && nums[nums[i] - 1] != nums[i]) 
            {
                int tmp = nums[nums[i]-1];
                nums[nums[i]-1] = nums[i];
                nums[i] = tmp;
            }
        }
        for(int i=0; i<nums.length; i++)
        {
            if(nums[i] != i+1) result.add(i+1);
        }
        return result;
    }
}