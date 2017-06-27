/*
* @Author: WuLC
* @Date:   2017-06-27 17:58:05
* @Last Modified by:   WuLC
* @Last Modified time: 2017-06-27 18:13:16
* @Email: liangchaowu5@gmail.com
*/


// O(1) space but ugly code
public class Solution 
{
    public boolean canPlaceFlowers(int[] flowerbed, int n)
    {
        int count = 0;
        if (flowerbed.length == 1)
        {
            if (flowerbed[0] == 0) count++;
        }
        else
        {
            for (int i = 0; i < flowerbed.length; i++)
            {
                if (flowerbed[i] == 1) continue;
                else if(i == 0)
                {
                    if (flowerbed[i+1] == 0)
                    {
                        flowerbed[i] = 1;
                        count += 1;
                    }
                }
                else if (i == flowerbed.length -1)
                {
                    if (flowerbed[i-1] == 0)
                    {
                        flowerbed[i] = 1;
                        count += 1;
                    }
                }
                else if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0)
                {
                    flowerbed[i] = 1;
                    count += 1;
                }
            }
        }
        if (count >= n) return true;
        return false;
    }
}

// O(n) space but concise code
public class Solution 
{
    public boolean canPlaceFlowers(int[] flowerbed, int n) 
    {
        int[] flower = new int[flowerbed.length+2];
        flower[0] = 0;
        flower[flower.length-1] = 0;
        for(int i = 0; i < flowerbed.length; i++) flower[i+1] = flowerbed[i];
        
        int count = 0;
        for (int i = 1; i < flower.length-1; i++)
        {
            if (flower[i] == 0 && flower[i-1] == 0 && flower[i+1] == 0)
            {
                flower[i] = 1;
                count++;
            }
            if (count >= n) return true;
        }
        return false;
    }
}