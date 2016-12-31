/**
* Author: WuLC
* Date:   2016-12-31 14:36:14
* Last modified by:   WuLC
* Last Modified time: 2016-12-31 14:42:31
* Email: liangchaowu5@gmail.com
*/

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start 
 * = s; end = e; }
 * }
 */

// sort the intervals and then merge them
public class Solution 
{
    public List<Interval> merge(List<Interval> intervals) 
    {
        List<Interval> result = new ArrayList<Interval>();
        if (intervals.size() == 0) return result;
        // sort the list of intervals
        Collections.sort(intervals, new Comparator<Interval>() 
        {
            @Override
            public int compare(Interval o1, Interval o2) 
            {
                if (o1.start != o2.start) return o1.start- o2.start;
                else return o1.end- o2.end;
            }
        });
        
        int currStart = intervals.get(0).start, currEnd = intervals.get(0).end;
        Interval tmp = new Interval();
        for(int i=1; i<intervals.size(); i++)
        {
            tmp = intervals.get(i);
            if (currEnd >= tmp.start) currEnd = Math.max(tmp.end,currEnd);
            else
            {
                result.add(new Interval(currStart, currEnd));
                currStart = tmp.start;
                currEnd = tmp.end;
            }
        }
        result.add(new Interval(currStart, currEnd));
        return result;
    }
}