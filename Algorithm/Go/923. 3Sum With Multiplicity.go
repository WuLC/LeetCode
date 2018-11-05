/*
 * Created on Mon Nov 05 2018 22:3:4
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// count the number of two sum, O(n^2) time complexity
func threeSumMulti(A []int, target int) int {
	result := 0
	counter := make(map[int]int)
	for i, num := range A {
		result = (result + counter[target-num]) % 1000000007
		for j := 0; j < i; j++ {
			counter[A[i]+A[j]]++
		}
	}
	return result
}