/*
 * Created on Thu Nov 09 2017 8:29:31
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// binary
// find the cloest heater for each house and return the distance
class Solution 
{
    public int findRadius(int[] houses, int[] heaters) 
    {
        Arrays.sort(heaters);
        int result = 0;
        for(int i=0; i<houses.length; i++)
        {
            result = Math.max(result, binarySearch(heaters, houses[i]));   
        }
        return result;
    }
    
    public int binarySearch(int[] heaters, int house)
    {
        int left = 0, right = heaters.length - 1;
        while(left < right-1)
        {
            int mid = left + ((right-left)>>1);
            if(heaters[mid] == house) return 0;
            else if(heaters[mid] > house) right = mid;
            else left = mid;
        }
        return Math.min(Math.abs(heaters[left]-house),
                        Math.abs(heaters[right]-house));
    }
}