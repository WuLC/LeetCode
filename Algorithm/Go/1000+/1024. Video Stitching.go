/*
 * Created on Wed Apr 10 2019 17:59:17
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy with two pointers

import "sort"

func videoStitching(clips [][]int, T int) int {
	record := make(map[int]int)
	keys := []int{}
	for _, c := range clips {
		if value, exist := record[c[0]]; exist {
			record[c[0]] = max(value, c[1])
		} else {
			record[c[0]] = c[1]
			keys = append(keys, c[0])
		}
	}
	sort.Ints(keys)
	curr, next, count := 0, 0, 0
	for _, k := range keys {
		if curr >= T || next < k {
			break
		}
		if curr < k {
			count++
			curr = next
		}
		next = max(next, record[k])
	}
	if curr >= T {
		return count
	} else if next >= T {
		return count + 1
	} else {
		return -1
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}