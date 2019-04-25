/*
 * Created on Wed Apr 24 2019 15:9:9
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// dp, O(nlgn) time, O(n) space
// next great element with TreeMap, but leetcode platform do not install this package
import "github.com/emirpasic/gods/maps/treemap"

func oddEvenJumps(A []int) int {
	n := len(A)
	m := treemap.NewWithIntComparator()
	odd_dp, even_dp := make([]bool, n), make([]bool, n)
	odd_dp[n-1], even_dp[n-1] = true, true
	result := 1
	for i := n - 2; i >= 0; i-- {
		if k, v := m.Ceiling(A[i]); k != nil {
			odd_dp[i] = even_dp[v]
		}
		if k, v := m.Floor(A[i]); k != nil {
			even_dp[i] = odd_dp[v]
		}
		if odd_dp[i] {
			result++
		}
		m.Put(A[i], i)
	}
	return result
}

