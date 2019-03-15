/*
 * Created on Fri Mar 15 2019 17:41:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution, O(n) time

func minDominoRotations(A []int, B []int) int {
	c1, c2 := minSwap(A[0], A, B), minSwap(B[0], A, B)
	if c1 == -1 {
		return c2
	} else if c2 == -1 {
		return c1
	} else {
		return min(c1, c2)
	}
}

func minSwap(target int, A []int, B []int) int {
	num_A, num_B := 0, 0
	for i := 0; i < len(A); i++ {
		if A[i] != target && B[i] != target {
			return -1
		}
		if A[i] != target {
			num_A++
		}
		if B[i] != target {
			num_B++
		}
	}
	return min(num_A, num_B)
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}