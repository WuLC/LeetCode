/*
* @Author: WuLC
* @Date:   2017-05-26 20:25:32
* @Last Modified by:   WuLC
* @Last Modified time: 2017-05-26 20:26:53
* @Email: liangchaowu5@gmail.com
*/


// the result has at most two numbers ,find the possible two numbers 
// then traverse the array again to check whether it is legal
public class Solution 
{
    public List<Integer> majorityElement(int[] nums) 
    {
        int count1 = 0, count2 = 0, num1 = 0, num2 = 0;
        for(int num : nums)
        {
            if (count1 == 0 && (count2 == 0 || num2 != num))
            {
                num1 = num;
                count1++;
                continue;
            }
            if (count2 == 0 && (count1 == 0 || num1 != num))
            {
                num2 = num;
                count2++;
                continue;
            }
            
            if(num == num1) count1++;
            else if(num == num2) count2++;
            else
            {
                count1--;
                count2--;
            }
        }
        
        List<Integer> result = new ArrayList<Integer>();
        count1 = 0;
        count2 = 0;
        for(int num : nums)
        {
            if(num == num1) count1++;
            if(num == num2) count2++;
        }
        if(count1 > nums.length/3) result.add(num1);
        if(count2 > nums.length/3 && num1 != num2) result.add(num2);
        return result;
    }
}