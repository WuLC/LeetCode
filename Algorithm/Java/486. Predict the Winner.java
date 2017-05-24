/**
* Author: WuLC
* Date:   2017-05-24 12:50:26
* Last modified by:   WuLC
* Last Modified time: 2017-05-24 12:52:40
* Email: liangchaowu5@gmail.com
*/


// recursive 
// P1Win represent whether P1 can win with the game with the left numbers
// P2Win represent whether P2 can win with the game with the left numbers
public class Solution 
{
    public boolean PredictTheWinner(int[] nums) 
    {
        return P1Win(nums, 0, nums.length - 1, 0, 0);
    }
    
    public boolean P1Win(int[] nums, int start, int end, int sum1, int sum2)
    {
        if (start > end)
        {
            if(sum1 >= sum2) return true;
            else return false;
        }
        if (P2Win(nums, start+1, end, sum1+nums[start], sum2) && P2Win(nums, start, end-1, sum1+nums[end], sum2)) return false;
        else return true;
    }
    
    public boolean P2Win(int[] nums, int start, int end, int sum1, int sum2)
    {
        if (start > end)
        {
            if(sum2 > sum1) return true;
            else return false;
        }
        if (P1Win(nums, start+1, end, sum1, sum2+nums[start]) && P1Win(nums, start, end-1, sum1, sum2+nums[end])) return false;
        else return true;
    }
}