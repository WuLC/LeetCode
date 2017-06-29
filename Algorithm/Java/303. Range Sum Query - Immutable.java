/*
* @Author: WuLC
* @Date:   2017-06-29 09:35:38
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-29 09:39:57
* @Email: liangchaowu5@gmail.com
*/


// calculate presum, with or without additional element is OK
// without additional elemnt
public class NumArray 
{
    private int[] preSum;
    
    public NumArray(int[] nums) 
    {
        preSum = new int[nums.length];
        for(int i = 0; i < nums.length; i++)
        {
            if(i == 0) preSum[i] = nums[i];
            else preSum[i] = preSum[i-1] + nums[i];
        }
    }
    
    public int sumRange(int i, int j) 
    {
        if (i == 0) return preSum[j];
        else return preSum[j] - preSum[i-1];
    }
}


// with additional element
public class NumArray 
{
    private int[] preSum;
    
    public NumArray(int[] nums) 
    {
        preSum = new int[nums.length + 1];
        for(int i = 0; i < nums.length; i++)
            preSum[i + 1] = preSum[i] + nums[i];
    }
    
    public int sumRange(int i, int j) 
    {
        return preSum[j+1] - preSum[i];
    }
}
