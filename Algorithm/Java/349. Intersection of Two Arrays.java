/*
* @Author: WuLC
* @Date:   2017-07-01 17:29:07
* @Last Modified by:   WuLC
* @Last Modified time: 2017-07-01 17:29:27
* @Email: liangchaowu5@gmail.com
*/

// use two sets, O(n) time
public class Solution 
{
    public int[] intersection(int[] nums1, int[] nums2) 
    {
        Set<Integer> nums1Set = new HashSet<Integer>();
        Set<Integer> nums2Set = new HashSet<Integer>();
        for (int num:nums1) nums1Set.add(num);
        for (int num:nums2) nums2Set.add(num);
      		
        nums1Set.retainAll(nums2Set); // nums1Set now contains only elements in both sets
        int[] result = new int[nums1Set.size()];
        int i = 0;
        for(int num : nums1Set) result[i++] = num;
        return result;
    }
}