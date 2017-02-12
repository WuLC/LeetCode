/*
* @Author: WuLC
* @Date:   2017-02-12 21:54:05
* @Last Modified by:   WuLC
* @Last Modified time: 2017-02-12 21:55:42
* @Email: liangchaowu5@gmail.com
*/

// stack and hashmap, similar to 500. Next Greater Element I
// traverse two times, the second time is to find the next greater number for the numbers thar are still in the stack
public class Solution 
{
    public int[] nextGreaterElements(int[] nums) 
    {
        int[] result = new int[nums.length];
        Stack<Integer> stack = new Stack<Integer>();
        Map<Integer, Stack<Integer>> numsMap = new HashMap<Integer, Stack<Integer>>();
        
        for (int i=0; i<2; i++)
        {
            for(int num:nums)
            {
                while(!stack.isEmpty() && stack.peek() < num)
                {
                    int tmp = stack.pop();
                    if(!numsMap.containsKey(tmp)) numsMap.put(tmp, new Stack<Integer>());
                    numsMap.get(tmp).push(num);
                }
                if(i == 0) stack.push(num);
            }
        }
        
        for(int i=nums.length - 1; i >= 0; i--)
        {
            if(numsMap.containsKey(nums[i])) result[i] = numsMap.get(nums[i]).pop();
            else result[i] = -1;
        }
        return result;
    }
}