/*
 * Created on Sun Oct 07 2018 20:28:5
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// modify string in place
class Solution {
public:
  string reverseOnlyLetters(string S) {
    for(int i = 0, j = S.size()-1; i < j; i++, j--) {
      while (i < j && !isalpha(S[i])) i++;
      while (i < j && !isalpha(S[j])) j--;
      if (i < j) std::swap(S[i], S[j]);
    }
    return S;
  }
};