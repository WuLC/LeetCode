/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 */

// @lc code=start
#include <iostream>
#include <list>
#include <unordered_map>


class LRUCache {
public:
    LRUCache(int capacity): _maxSize(capacity) {
    }
    
    int get(int key) {
        if (index.find(key) == index.end()) {
            return -1;
        }
        int value = index[key].first;
        nodes.erase(index[key].second);
        nodes.push_front(key);
        index[key] = {value, nodes.begin()};
        return value;
    }
    
    void put(int key, int value) {
        if (index.find(key) == index.end()) {
            if (index.size() == _maxSize) {
                index.erase(nodes.back());
                nodes.pop_back();
            }
        } else {
            nodes.erase(index[key].second);
        }
        nodes.push_front(key);
        index[key] = {value, nodes.begin()};
    }
    
    void show() {
        for(auto it = nodes.begin(); it != nodes.end(); it++) {
            std::cout << *it << std::endl;
        }
    }

private:
    std::list<int> nodes;
    std::unordered_map<int, std::pair<int, std::list<int>::iterator>> index;
    int _maxSize;
};


// @lc code=end

