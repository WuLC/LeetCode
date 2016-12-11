/**
* Author: WuLC
* Date:   2016-12-11 16:31:43
* Last modified by:   WuLC
* Last Modified time: 2016-12-11 16:42:46
* Email: liangchaowu5@gmail.com
*/

// count the water that each position can store and add them up
// the amount of water of a certain postion is determined by the highest bar on its' left side, the hightest bar on its' right side as well as its height 
// time O(n)
public class Solution 
{
    public int trap(int[] height) 
    {
        int[] maxHeight = new int[height.length]; // maxHeight[i] represents the max height among height[i:]
        int result = 0, currMax = 0;
        for (int i=height.length-1; i>=0; i--)
        {
            currMax = Math.max(currMax, height[i]);
            maxHeight[i] = currMax;
        }
        
        currMax = 0;
        for(int i=0; i < height.length; i++)
        {
            currMax = Math.max(height[i], currMax);
            if (height[i] < currMax && height[i] < maxHeight[i]) 
                result += (Math.min(currMax, maxHeight[i]) - height[i]);
        }
        return result;
    }
}