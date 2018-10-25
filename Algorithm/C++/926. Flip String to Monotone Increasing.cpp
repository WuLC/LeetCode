/*
 * Created on Thu Oct 25 2018 9:43:58
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// O(n) time, O(1) space
// at each index, flip all 1s on its left and 0s on its right
class Solution {
 public:
    int minFlipsMonoIncr(string S) {
      int left = 0, right = 0;
      for(char c : S) {
        if (c == '0') right++;
      }
      int result = right;
      for(char c : S) {
        if (c == '1')
          left++;
        else
          right--;
        result = std::min(result, left + right);
      }
      return result;
    }
};