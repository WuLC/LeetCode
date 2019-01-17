/*
 * Created on Thu Jan 17 2019 9:34:55
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// prefix sum with mod count
func subarraysDivByK(A []int, K int) int {
	mod_count := make([]int, K)
	mod_count[0] = 1
	prefix, result := 0, 0
	for _, num := range A {
		prefix = (prefix + num) % K
		if prefix < 0 {
			prefix += K
		}
		result += mod_count[prefix]
		mod_count[prefix]++
	}
	return result
}