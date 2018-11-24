/*
 * Created on Sat Nov 24 2018 8:57:29
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple solution
func minDeletionSize(A []string) int {
	count := 0
	m, n := len(A), len(A[0])
	for i := 0; i < n; i++ {
		for j := 1; j < m; j++ {
			if A[j][i] < A[j-1][i] {
				count++
				break
			}
		}
	}
	return count
}