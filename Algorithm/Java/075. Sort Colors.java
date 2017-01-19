/*
* @Author: WuLC
* @Date:   2017-01-16 09:41:06
* @Last Modified by:   WuLC
* @Last Modified time: 2017-01-16 10:22:40
* @Email: liangchaowu5@gmail.com
*/

// method 1, count and fill the array without sorting
public class Solution 
{
    public void sortColors(int[] nums) 
    {
        int[] colorCount = new int[3];
        for(int i=0; i < nums.length; i++)
            colorCount[nums[i]]++;
        Arrays.fill(nums, 0, colorCount[0], 0);
        Arrays.fill(nums, colorCount[0], colorCount[0]+colorCount[1], 1);
        Arrays.fill(nums, colorCount[0]+colorCount[1], nums.length, 2);
    }
}

//method 2, tow pointers, move 2 to the end and 1 to the head
public class Solution 
{
    public void sortColors(int[] nums) 
    {
    	int p1 = 0, p2 = nums.length-1;
        for(int i = 0; i < nums.length; i++)
        {
        	while(nums[i] == 2 && i <= p2)  swap(nums, i, p2--);
        	while(nums[i] == 0 && i >= p1)  swap(nums, i, p1++);
        }
    }

    private void swap(int[] nums, int a, int b)
    {
    	int tmp = nums[a];
    	nums[a] = nums[b];
    	nums[b] = tmp;
    }
}