#include <vector>
#include <cmath>

class UnionFindSet {
 public:
    UnionFindSet(int n) {
        for (int i = 0; i < n; i++) {
            parent.push_back(i);
            height.push_back(0);
        }
    }

    int find(int v) {
        if (parent[v] != v) parent[v] = find(parent[v]);
        return parent[v];
    }

    void union_(int p1, int p2) {
        if (height[p1] == height[p2]) {
            parent[p2] = p1;
            height[p1]++;
        } else if (height[p1] > height[p2]) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
        }
    }

 private:
    std::vector<int> parent;
    std::vector<int> height;
};

class Solution {
public:
    int minCostConnectPoints(std::vector<std::vector<int>>& points) {
        std::vector<std::vector<int>> distance;
        int n = points.size();
        for (int i=0; i<n; i++)
            for (int j=i+1; j<n; j++)
                distance.push_back(std::vector{i, j, 
                                   std::abs(points[i][0] - points[j][0]) + std::abs(points[i][1] - points[j][1])});
        std::sort(distance.begin(), distance.end(), [](const std::vector<int>& v1, const std::vector<int>& v2){
            return v1[2] < v2[2];
        });

        UnionFindSet ufs(n);
        int p1, p2, result = 0;
        for (auto d:distance) {
            p1 = ufs.find(d[0]);
            p2 = ufs.find(d[1]);
            if (p1 != p2) {
                result += d[2];
                ufs.union_(p1, p2);
            }
        }
        return result;
    }
};


