/**
* Author: WuLC
* Date:   2016-11-26 15:31:11
* Last modified by:   WuLC
* Last Modified time: 2016-11-26 15:43:14
* Email: liangchaowu5@gmail.com
*/


// HashMap, Two pointers
// use hashmap to store the number of each current legal word
// use two pointers to maintain the possible substring
// use a counter to count the current legal words

// pay attention that all words are same length and duplicate word may appear int words
public class Solution 
{
    public List<Integer> findSubstring(String s, String[] words) 
    {
        List<Integer> result = new ArrayList<Integer>();
        if (words.length == 0 || s.length() == 0) return result;

        // count the number of different words
        Map<String, Integer> wordNum = new HashMap<String, Integer>();
        for (String word:words)
        {
            if (wordNum.containsKey(word)) wordNum.put(word, wordNum.get(word)+1);
            else wordNum.put(word, 1);
        }
        
        // store the number of each current legal word
        Map<String, Integer> currWords = new HashMap<String, Integer>();
        int wordLen = words[0].length();
        String word = null;
        for (int start=0; start < wordLen; start++)  // traverse all possible starting character
        {
            int left = start, right = start;
            int count = 0;
            currWords.clear();
            while (right+wordLen <= s.length())
            {
                word = s.substring(right, right+wordLen);
                if (!wordNum.containsKey(word))
                {
                    count = 0;
                    currWords.clear();
                    right += wordLen;
                    left = right; 
                }
                else
                {
                    if (!currWords.containsKey(word)) 
                        {
                            currWords.put(word, 1);
                            count += 1;
                        }
                    else 
                    {
                        currWords.put(word, currWords.get(word)+1);
                        count += 1;
                        if (currWords.get(word) > wordNum.get(word)) // number of current word is larger than its number in words
                        {
                            String tmp = "";
                            while (!tmp.equals(word))
                            {
                                tmp = s.substring(left, left+wordLen);
                                left += wordLen;
                                count -= 1;
                                currWords.put(tmp, currWords.get(tmp)-1);
                            }
                        }
                    }
                    
                    if (count == words.length)
                    {
                        result.add(left);
                        String tmp = s.substring(left, left+wordLen);
                        currWords.put(tmp, currWords.get(tmp)-1);
                        left += wordLen;
                        count -= 1;
                    }
                    right += wordLen;
                }
            }
        }
        return result;
    }
}