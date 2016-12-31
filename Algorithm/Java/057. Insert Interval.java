/**
* Author: WuLC
* Date:   2016-12-31 16:07:17
* Last modified by:   WuLC
* Last Modified time: 2016-12-31 16:10:23
* Email: liangchaowu5@gmail.com
*/

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */

// O(n) time, travserse once 
// three cases, read comments

public class Solution 
{
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) 
    {
        List<Interval> result = new ArrayList<Interval>();
        Interval tmp;
        boolean added = false;
        int currStart, currEnd, i = 0;
        while(i < intervals.size())
        {
            tmp = intervals.get(i);
            // add initial interval in intervals
            if (newInterval.start > tmp.end || added == true) 
            {
                result.add(tmp);
                i++;
            }
            // add newInterval
            else if (tmp.start > newInterval.end)  
            {
                result.add(newInterval);
                added = true;
            }
            // merge newInterval with initial interval and add it
            else                                  
            {
                currStart = Math.min(tmp.start, newInterval.start);
                currEnd = Math.max(tmp.end, newInterval.end);
                while (i < intervals.size() && currEnd >= intervals.get(i).start)
                {
                    currEnd = Math.max(currEnd, intervals.get(i).end);
                    i++;
                }
                result.add(new Interval(currStart, currEnd));
                added = true;
            }
        }
        if (added == false) result.add(newInterval);
        return result;
    }
}