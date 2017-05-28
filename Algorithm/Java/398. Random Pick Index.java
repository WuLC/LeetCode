/*
* @Author: WuLC
* @Date:   2017-05-28 14:29:16
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-28 14:30:40
* @Email: liangchaowu5@gmail.com
*/


// Reservoir Sampling
// O(n) time, O(1) space
public class Solution 
{  
    private int[] numbers;

    public Solution(int[] nums) 
    {
        numbers = nums;
    }
    
    public int pick(int target) 
    {
        int index = 0, count = 0;
        for(int i = 0; i < numbers.length; i++)
        {
            if (numbers[i] == target)
            {
                count++;
                if(Math.random() < 1.0/count) index = i;
            }
        }
        return index;
    }
}