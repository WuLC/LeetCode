/**
* Author: WuLC
* Date:   2017-05-13 10:16:06
* Last modified by:   WuLC
* Last Modified time: 2017-05-13 10:16:52
* Email: liangchaowu5@gmail.com
*/


// dfs, add city from the end of itinerary
public class Solution 
{
    private Map<String, List<String>> mapping;
    private List<String> result;

    public List<String> findItinerary(String[][] tickets) 
    {
        mapping = new HashMap<String, List<String>>();
        result = new ArrayList<String>();
        
        for(int i=0; i < tickets.length; i++)
        {
            if (!mapping.containsKey(tickets[i][0])) mapping.put(tickets[i][0], new ArrayList<String>());
            mapping.get(tickets[i][0]).add(tickets[i][1]);
        }
        // sort 
        for(Map.Entry<String, List<String>> entry : mapping.entrySet())
        {
            Collections.sort(entry.getValue(), new Comparator<String>(){
                @Override
                public int compare(String s1, String s2)
                {
                    if(s1.compareTo(s2) > 0) return -1;
                    else return 1;
                }
            });
        }
        dfs("JFK");
        Collections.reverse(result);
        return result;
    }
    
    private void dfs(String curr)
    {
        List<String> tmp;
        String next;
        while (mapping.containsKey(curr) && mapping.get(curr).size() > 0)
        {
            tmp = mapping.get(curr);
            next = tmp.get(tmp.size()-1);
            tmp.remove(tmp.size()-1);
            dfs(next);
        }
        result.add(curr);
    }
}