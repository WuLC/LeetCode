/**
* Author: WuLC
* Date:   2017-05-06 16:02:43
* Last modified by:   WuLC
* Last Modified time: 2017-05-06 16:04:19
* Email: liangchaowu5@gmail.com
*/


// sort the points firstly then count the number of duplicated parts
public class Solution 
{
    public int findMinArrowShots(int[][] points) 
    {
        Arrays.sort(points, new Comparator<int[]>(){
           @Override
           public int compare(int[] a, int[] b)
           {
               if (a[0] != b[0]) return a[0] - b[0];
               else return a[1] - b[1];
           }
        });
        
        int count = 0;
        int[] curr = new int[2];
        for (int i = 0; i < points.length; i++)
        {
            if (i == 0 || points[i][0] > curr[1])
            {
                count += 1;
                curr[0] = points[i][0];
                curr[1] = points[i][1];
            }
            else
            {
                curr[0] = points[i][0];
                curr[1] = Math.min(curr[1], points[i][1]);
            }
        }
        return count;
    }
}