/*
* @Author: WuLC
* @Date:   2017-02-12 21:31:25
* @Last Modified by:   WuLC
* @Last Modified time: 2017-02-12 21:32:03
* @Email: liangchaowu5@gmail.com
*/

// stack, O(n) time, O(n) space
public class Solution 
{
    public int[] nextGreaterElement(int[] findNums, int[] nums)
    {
        int[] result = new int[findNums.length];
        Map<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
        Stack<Integer> s = new Stack<Integer>();
        for(int num:nums)
        {
            while (!s.isEmpty() && s.peek() < num)
                numsMap.put(s.pop(), num);
            s.push(num);
        }
        for(int i=0; i<findNums.length; i++)
        {
            if(numsMap.containsKey(findNums[i])) result[i] = numsMap.get(findNums[i]);
            else result[i] = -1;
        }
        return result;
        
    }
}