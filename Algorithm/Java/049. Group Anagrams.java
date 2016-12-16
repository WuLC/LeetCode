/**
* Author: WuLC
* Date:   2016-12-16 22:18:34
* Last modified by:   WuLC
* Last Modified time: 2016-12-16 22:22:12
* Email: liangchaowu5@gmail.com
*/


// sort each word in alphabetical order, use it as key in a hashtable 
public class Solution 
{
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        Map<String, List<String>> words= new HashMap<String, List<String>>();
        for(int i = 0; i < strs.length; i++)
        {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            // String keyStr = String.valueOf(chars); 
            // or
            String keyStr = new String(chars);
            if (!words.containsKey(keyStr)) words.put(keyStr, new ArrayList<String>());
            words.get(keyStr).add(strs[i]);
        }
        return new ArrayList<List<String>>(words.values()); //wrods.valuse() return collection<V> 
    }
}