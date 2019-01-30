/*
 * Created on Wed Jan 30 2019 22:36:20
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <string>

using std::string;

class Solution {
 public:
  string strWithout3a3b(int A, int B) {
    string result = "";
    while (A > 0 || B > 0) {
      if (A == B) {
        result += "ab";
        A--;
        B--;
      } else if (A > B) {
        result += A>1 ? "aa" : "a";
        A -= 2;
        result += B>0 ? "b" : "";
        B -= 1;
      } else {
        result += B>1 ? "bb" : "b";
        B -= 2;
        result += A>0 ? "a" : "";
        A -= 1;
      }
    }
    return result;
  }
};