/*
 * Created on Tue Oct 23 2018 20:30:50
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy, think with stack
class Solution {
public:
    int minAddToMakeValid(string S) {
      int left = 0, right = 0, result = 0;
      for(char c : S) {
        if(c == '(')
          left += 1;
        else {
          if(left == 0)
            result += 1;
          else
            left -= 1;
        }
      }
      result += left;
      return result;
    }
};