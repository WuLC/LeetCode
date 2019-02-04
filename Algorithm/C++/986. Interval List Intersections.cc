/*
 * Created on Mon Feb 04 2019 12:3:4
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

// two pointers
#include <vector>

using std::vector;

class Solution {
 public:
  vector<Interval> intervalIntersection(vector<Interval>& A, vector<Interval>& B) {
    vector<Interval> result;
    int p1 = 0, p2 = 0;
    while (p1<A.size() && p2<B.size()) {
      if (A[p1].start > B[p2].end) {
        p2++;
      } else if (A[p1].end < B[p2].start) {
        p1++;
      } else {
        int s = std::max(A[p1].start, B[p2].start);
        int e = std::min(A[p1].end, B[p2].end);
        result.push_back(Interval(s, e));
        if (A[p1].end < B[p2].end) {
          p1++;
        } else {
          p2++;
        }
      }
    }
    return result;
  }
};