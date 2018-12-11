/*
 * Created on Sat Dec 08 2018 20:8:58
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// permutataion
package main

import "fmt"

func largestTimeFromDigits(A []int) string {
	result := []string{""}
	permute(A, 0, len(A)-1, result)
	return result[0]
}

func permute(A []int, left int, right int, result []string) {
	if left == right {
		if A[0]*10+A[1] < 24 && A[2] < 6 {
			cand := fmt.Sprintf("%d%d:%d%d", A[0], A[1], A[2], A[3])
			if cand > result[0] {
				result[0] = cand
			}
		}
	}
	for i := left; i <= right; i++ {
		A[i], A[left] = A[left], A[i]
		permute(A, left+1, right, result)
		A[i], A[left] = A[left], A[i]
	}
}
