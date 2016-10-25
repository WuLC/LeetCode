/**
* Author: WuLC
* Date:   2016-10-25 17:12:21
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 17:13:38
* Email: liangchaowu5@gmail.com
*/


// sort and then two pointers, time complexity(O(n^3))
// use set instead list to store the result as there may be duplicates
public class Solution 
{
    public List<List<Integer>> fourSum(int[] nums, int target) 
    {
        Set<List<Integer>> result = new HashSet<List<Integer>>();
        int sum, left, right;
        
        Arrays.sort(nums);
        for (int i=0; i<nums.length-3;i++)
        {
            for (int j=i+1; j<nums.length-2; j++)
            {
                sum = 0; left = j+1; right = nums.length-1;
                sum += (nums[i] + nums[j]);
                while (left < right)
                {
                    if (sum + nums[left] + nums[right] == target)
                    {
                        result.add(new ArrayList(Arrays.asList(nums[i], nums[j], nums[left], nums[right])));
                        left++;
                        right--;
                        // can't break here, since the problem need to find all possible result
                    }
                    else if (sum + nums[left] + nums[right] > target) right--;
                    else left++;
                }
            }
        }
        return new ArrayList(result); // convert set to arraylist
    }
}