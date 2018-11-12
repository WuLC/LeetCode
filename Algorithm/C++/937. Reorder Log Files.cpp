/*
 * Created on Sun Nov 11 2018 14:34:52
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// with extract space
class Solution {
 public:
    vector<string> reorderLogFiles(vector<string>& logs) {
      vector<string> letter_logs, digital_logs;
      for(auto s : logs) {
        if (isdigit(s.back())) 
          digital_logs.push_back(s);
        else 
          letter_logs.push_back(s);
      }
      std::sort(letter_logs.begin(), letter_logs.end(), cmp);
      letter_logs.insert(letter_logs.end(), digital_logs.begin(), digital_logs.end());
      return letter_logs;
    }
  
  private:
    static bool cmp(string& s1, string& s2) {
      return s1.substr(s1.find(' ')) < s2.substr(s2.find(' '));
    }
};

// without extract space
class Solution {
 public:
    vector<string> reorderLogFiles(vector<string>& logs) {
      int p1 = logs.size() - 1, p2 = logs.size() - 1;
      while (p1 >= 0 && p1 <= p2) {
        while(p2 >= 0 && std::isdigit(logs[p2].back())) p2--;
        p1 = p2 - 1;
        while(p1 >= 0 && !std::isdigit(logs[p1].back())) p1--;
        if (p1 >= 0) std::swap(logs[p1], logs[p2]);
      }
      if (std::isdigit(logs[p2].back()))
        std::sort(logs.begin(), logs.begin() + p2, cmp);
      else
        std::sort(logs.begin(), logs.begin() + p2 + 1, cmp);
      return logs;
    }

 private:
    static bool cmp(string& s1, string& s2) {
      return s1.substr(s1.find(' ')) < s2.substr(s2.find(' '));
    }
};