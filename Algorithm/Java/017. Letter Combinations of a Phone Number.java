/**
* Author: WuLC
* Date:   2016-10-25 14:50:21
* Last modified by:   WuLC
* Last Modified time: 2016-10-25 14:50:48
* Email: liangchaowu5@gmail.com
*/

public class Solution 
{
    private static final Map<Character, String> map= new HashMap<Character, String>();
    static // init a static hash map
    {
        map.put('2',"abc");
        map.put('3',"def");
        map.put('4',"ghi");
        map.put('5',"jkl");
        map.put('6',"mno");
        map.put('7',"pqrs");
        map.put('8',"tuv");
        map.put('9',"wxyz");
    }
    
    public List<String> letterCombinations(String digits) 
    {
        List<String> result = new ArrayList<String>();
        List<String> tmp = new ArrayList<String>();
        char c = ' ';
        String s = "";
        for (int i=0; i < digits.length(); i++)
        {
            c = digits.charAt(i);
            if (c == '1' || c=='0') continue;
            s = map.get(c);
            for (int j = 0; j < s.length(); j++)
            {
                if (result.size() == 0)  result.add("");
                for(String str:result) 
                    tmp.add(str+s.charAt(j));
            }
            result = new ArrayList(tmp);
            tmp.clear();
        }
        return result;
    }
}