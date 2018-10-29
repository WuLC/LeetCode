/*
 * Created on Sun Oct 28 2018 17:8:57
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
class Solution {
 public:
    int numUniqueEmails(vector<string>& emails) {
      set<string> result;
      for(auto email : emails) {
        string tmp = "";
        int idx = 0;
        bool abandon = false;
        while (email[idx] != '@'){
          if (email[idx] == '+')
            abandon = true;
          else if (abandon == false && email[idx] != '.')
            tmp += email[idx];
          idx += 1;
        }
        tmp += email.substr(idx);
        result.insert(tmp);
      }
      return result.size();
    }
};