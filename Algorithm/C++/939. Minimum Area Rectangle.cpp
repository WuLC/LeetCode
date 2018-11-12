/*
 * Created on Mon Nov 12 2018 17:24:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// create index with hashmap
class Solution {
 public:
  int minAreaRect(vector<vector<int>>& points) {
    // std::unordered_map<int, std::set<int>> x_index;
    // std::vector<int> xs;
    // for (auto p : points) x_index[p[0]].insert(p[1]);
    // for (auto kv : x_index) xs.push_back(kv.first);
    // std::sort(xs.begin(), xs.end());

    // map can be used too, the fllowing code can replace the above code
    std::map<int, std::set<int>> x_index;
    std::vector<int> xs;
    for (auto p : points) x_index[p[0]].insert(p[1]);
    for (auto kv : x_index) xs.push_back(kv.first);

    int area = 1600000001;
    for (int i = 0; i < xs.size(); ++i) {
      for (int j = i + 1; j < xs.size(); ++j) {
        vector<int> legal_y;
        for(auto key : x_index[xs[i]]) {
          if (x_index[xs[j]].count(key) > 0)
            legal_y.push_back(key);
        }
        std::sort(legal_y.begin(), legal_y.end());
        if (legal_y.size() > 1) {
          int min_y_interval = legal_y[1] - legal_y[0];
          for(int k = 1; k < legal_y.size(); ++k) 
            min_y_interval = std::min(min_y_interval, legal_y[k] - legal_y[k-1]);
          area = std::min(area, (xs[j] - xs[i]) * min_y_interval);
        }
      }
    }
    if (area != 1600000001) 
      return area;
    else
      return 0;
  }
};