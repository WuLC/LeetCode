/*
 * Created on Tue Oct 23 2018 16:44:51
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
class Solution {
public:
    bool isLongPressedName(string name, string typed) {
      int idx1 = 0, idx2 = 0, n1 = name.size(), n2 = typed.size();
      while(idx1 < n1 and idx2 < n2) {
        if (name[idx1] != typed[idx2]) return false;
        int cnt1 = 1, cnt2 = 1;
        while(idx1+1 < n1 && name[idx1+1] == name[idx1]) {
          idx1 += 1;
          cnt1 += 1;
        }
        while(idx2+1 < n2 && typed[idx2+1] == typed[idx2]) {
          idx2 += 1;
          cnt2 += 1;
        }
        if (cnt1 > cnt2) return false;
        idx1 += 1;
        idx2 += 1;
      }
      if (idx1 == n1 && idx2 == n2)
        return true;
      else
        return false;
    }
};