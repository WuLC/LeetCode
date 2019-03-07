/*
 * Created on Thu Mar 07 2019 22:21:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// use two hashmap, one for timestamp, the other for value
type TimeMap struct {
	TimeDB  map[string][]int
	ValueDB map[string][]string
}

/** Initialize your data structure here. */
func Constructor() TimeMap {
	return TimeMap{make(map[string][]int), make(map[string][]string)}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	if _, present := this.TimeDB[key]; !present {
		this.TimeDB[key] = []int{}
		this.ValueDB[key] = []string{}
	}
	this.TimeDB[key] = append(this.TimeDB[key], timestamp)
	this.ValueDB[key] = append(this.ValueDB[key], value)
}

func (this *TimeMap) Get(key string, timestamp int) string {
	if val, present := this.TimeDB[key]; !present || val[0] > timestamp {
		return ""
	}
	idx := this.BinarySearch(key, timestamp)
	return this.ValueDB[key][idx]
}

func (this TimeMap) BinarySearch(key string, timestamp int) int {
	left, right := 0, len(this.TimeDB[key])-1
	for left < right {
		mid := left + ((right - left) >> 1)
		if this.TimeDB[key][mid] == timestamp {
			left = mid
			break
		} else if this.TimeDB[key][mid] < timestamp {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	if this.TimeDB[key][left] <= timestamp {
		return left
	} else {
		return left - 1
	}
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */