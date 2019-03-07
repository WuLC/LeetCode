/*
 * Created on Thu Mar 07 2019 21:16:26
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

#include <unordered_map>
#include <vector>
#include <string>

using std::string;
using std::vector;
using std::unordered_map;

// solution 1, use only one hashmap: unordered_map<key, vector<time, value>>
class TimeMap {
 public: 
  void set(string key, string value, int timestamp) {
    if (db.count(key) == 0) db[key] = vector<std::pair<int, string>> {};
    db[key].push_back(std::make_pair(timestamp, value));
  }
  
  string get(string key, int timestamp) {
    if (db.count(key) == 0 || db[key][0].first > timestamp)  return "";
    int idx = binary_search(key, timestamp);
    return db[key][idx].second;
  }

  int binary_search(string key, int timestamp) {
    int left = 0, right = db[key].size() - 1;
    while (left < right) {
      int mid = left + ((right-left)>>1);
      if (db[key][mid].first == timestamp) {
        left = mid;
        break;
      } else if (db[key][mid].first < timestamp) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return db[key][left].first <= timestamp? left: left-1;
  }

 private:
  std::unordered_map<string, vector<std::pair<int, string>>> db;
};


// solution 2, use two hashmap: unordered_map<key, vector<time>> and unordered_map<key, vector<value>>