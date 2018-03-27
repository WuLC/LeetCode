/*
 * Created on Tue Mar 27 2018 16:37:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// ensure that there are only two types of lengths and 0 is not in it(same points)
class Solution 
{
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) 
    {
        Set<Integer> allDist = new HashSet<Integer>(Arrays.asList(distance(p1, p2), distance(p1, p3), distance(p1, p4), 
                                                                  distance(p2, p3), distance(p2, p4), distance(p3, p4)));
        return allDist.size() == 2 && !allDist.contains(0); 
    }
    
    private int distance(int[] p1, int[] p2)
    {
        return (int)Math.pow(p1[0]-p2[0], 2.0) + (int)Math.pow(p1[1]-p2[1], 2.0);
    }
}