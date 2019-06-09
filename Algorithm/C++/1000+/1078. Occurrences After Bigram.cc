/*
 * Created on Sun Jun 09 2019 17:20:12
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
#include <vector>
#include <string>

using std::string;
using std::vector;

class Solution {
 public:
  vector<string> findOcurrences(string text, string first, string second) {
    vector<string> result, words = split(text, " ");
    for (int i = 0; i < words.size() - 2; i++) {
      if (words[i] == first && words[i+1] == second) {
        result.push_back(words[i+2]);
      }
    }
    return result;
  }

  vector<string> split(string s, string delimiter) {
    vector<string> words;
    size_t pos = 0;
    string token;
    while ((pos = s.find(delimiter)) != string::npos) {
      token = s.substr(0, pos);
      words.push_back(token);
      s.erase(0, pos+delimiter.size());
    }
    words.push_back(s);
    return words;
  }
};