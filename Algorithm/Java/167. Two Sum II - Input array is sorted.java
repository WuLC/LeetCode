/**
* Author: WuLC
* Date:   2016-10-09 19:26:10
* Last modified by:   WuLC
* Last Modified time: 2016-10-09 19:26:40
* Email: liangchaowu5@gmail.com
*/

// two pointers, O(n)
public class Solution 
{
    public int[] twoSum(int[] numbers, int target) 
    {
        int left = 0 , right = numbers.length-1;
        while (left < right)
        {   
            int sum = numbers[left] + numbers[right];
            if ( sum == target)
                break;
            else if (sum > target)
                right --;
            else
                left ++;
        }
        return new int[] {left+1, right+1};
    }
}