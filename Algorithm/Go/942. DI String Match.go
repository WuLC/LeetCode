/*
 * Created on Sat Nov 24 2018 9:40:52
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy
func diStringMatch(S string) []int {
	var result []int
	left, right := 0, len(S)
	for i := 0; i < len(S); i++ {
		if S[i] == 'I' {
			result = append(result, left)
			left++
		} else {
			result = append(result, right)
			right--
		}
	}
	result = append(result, left)
	return result
}