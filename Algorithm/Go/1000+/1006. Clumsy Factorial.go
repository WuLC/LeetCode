/*
 * Created on Fri Mar 15 2019 16:46:29
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, four numbers as a group

import "math"

func clumsy(N int) int {
	result := 0
	positive := true
	for N > 0 {
		tmp := 0
		if N >= 4 {
			if positive {
				tmp = int(math.Floor(float64(N*(N-1))/float64(N-2))) + (N - 3)
			} else {
				tmp = int(math.Floor(float64(N*(N-1))/float64(N-2))) - (N - 3)
			}
		} else if N == 3 {
			tmp = int(math.Floor(float64(N*(N-1)) / float64(N-2)))
		} else if N == 2 {
			tmp = N * (N - 1)
		} else {
			tmp = N
		}
		if positive {
			result += tmp
		} else {
			result -= tmp
		}
		positive = false
		N -= 4
	}
	return result
}