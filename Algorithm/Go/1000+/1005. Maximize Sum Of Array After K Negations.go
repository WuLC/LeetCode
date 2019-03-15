/*
 * Created on Thu Mar 14 2019 22:31:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy
// sort and

import "sort"

func largestSumAfterKNegations(A []int, K int) int {
	sort.Ints(A)
	idx := -1
	for i, v := range A {
		if v >= 0 {
			idx = i
			break
		}
	}
	result := 0
	if idx < 0 || idx >= K {
		for _, v := range A {
			if K > 0 {
				v *= -1
				K--
			}
			result += v
		}
	} else {
		left := (K - idx) & 1
		for i, v := range A {
			if i == idx && left > 0 {
				if idx > 0 && -1*A[i-1] < A[i] {
					result += 2 * A[i-1]
				} else {
					result += -2 * A[i]
				}
				left--
			}
			if v < 0 {
				v *= -1
			}
			result += v
		}
	}
	return result
}