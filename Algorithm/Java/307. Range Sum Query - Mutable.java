/*
* @Author: WuLC
* @Date:   2017-06-29 09:27:31
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-29 09:29:08
* @Email: liangchaowu5@gmail.com
*/


// binary indexed tree
// left index 0 unused
public class NumArray 
{
    private int[] numArray;
    private int[] BIT;
    
    public NumArray(int[] nums) 
    {
        numArray = new int[nums.length + 1];
        BIT = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++)
            update(i, nums[i]);
    }
    
    
    public void update(int i, int val) 
    {
        i += 1;
        int diff = val - numArray[i];
        numArray[i] = val;
        while(i < BIT.length)
        {
            BIT[i] += diff;
            i += (i & -i);
        }
    }
    
    
    public int leftSum(int i)
    {
        i += 1;
        int sum = 0;
        while(i > 0)
        {
            sum += BIT[i];
            i -= (i & -i);
        }
        return sum;
    }
    
    
    public int sumRange(int i, int j) 
    {
        return leftSum(j) - leftSum(i-1);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */