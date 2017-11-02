/*
 * Created on Thu Nov 02 2017 10:4:28
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
class Solution
{
    public String reverseVowels(String s) 
    {
        char[] cs = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        Set<Character> vowels = new HashSet<Character>();
        for (char ch:cs)
            vowels.add(ch);
        char[] chars = s.toCharArray();
        int left = 0, right = s.length() - 1;
        while (left<right)
        {
            while(left<right && !vowels.contains(chars[left])) left++;
            while(left<right && !vowels.contains(chars[right])) right--;
            if (left < right)
            {
                char tmp = chars[left];
                chars[left] = chars[right];
                chars[right] = tmp;
                left++;
                right--;
            }
        }
        return new String(chars);
    }
}