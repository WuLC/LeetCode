/*
 * Created on Mon Nov 26 2018 21:51:21
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

package main

import "sort"

// greedy, keep idx as current position to hold the next number
func minIncrementForUnique(A []int) int {
	idx, result := 40000, 0
	count := make(map[int]int)
	for i := 0; i < len(A); i++ {
		count[A[i]]++
		if idx > A[i] {
			idx = A[i]
		}
	}
	var keys []int
	for k, _ := range count {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	for _, k := range keys {
		if idx <= k {
			result += (count[k] * (count[k] - 1)) / 2
			idx = k + count[k]
		} else {
			result += (idx-k)*count[k] + (count[k]*(count[k]-1))/2
			idx += count[k]
		}
	}
	return result
}
