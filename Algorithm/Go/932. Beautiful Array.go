/*
 * Created on Wed Oct 31 2018 20:11:32
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// prefix sum, applicable to not just 1 and 0
func numSubarraysWithSum(A []int, S int) int {
	var curr_sum, result = 0, 0
	count := make(map[int]int)
	count[0] = 1
	for _, num := range A {
		curr_sum += num
		result += count[curr_sum-S]
		count[curr_sum] += 1
	}
	return result
}