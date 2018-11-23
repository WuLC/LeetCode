/*
 * Created on Fri Nov 23 2018 21:20:6
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// greedy
class Solution {
 public:
    vector<int> diStringMatch(string S) {
        vector<int> result;
        int left = 0, right = S.length();
        for (char c : S) {
          if (c == 'I') {
            result.push_back(left);
            left++;
          }
          else {
            result.push_back(right);
            right--;
          }
        }
        result.push_back(left);
        return result;
    }
};