/*
 * Created on Sun Feb 03 2019 17:45:51
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
func sumEvenAfterQueries(A []int, queries [][]int) []int {
	tmp := 0
	for _, v := range A {
		if (v&1) == 0 {
			tmp += v
		}
	}
	result := []int{}
	for _, q := range queries {
		if (A[q[1]]&1) == 0 && (q[0]&1) == 0 {
			tmp += q[0]
		} else if (A[q[1]]&1) == 1 && (q[0]&1) == 1 {
			tmp += A[q[1]] + q[0]
		} else if (A[q[1]]&1) == 0 && (q[0]&1) == 1 {
			tmp -= A[q[1]]
		}
		result = append(result, tmp)
		A[q[1]] += q[0]
	}
	return result
}