/*
 * Created on Mon Feb 25 2019 21:28:30
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// hashmap, simple solution
func findJudge(N int, trust [][]int) int {
	if N == 1 {
		return 1
	}
	result, count := -1, make(map[int]int)
	for _, t := range trust {
		count[t[1]]++
		if count[t[1]] == N-1 {
			if result < 0 {
				result = t[1]
			} else {
				return -1
			}
		}
	}
	for _, t := range trust {
		if t[0] == result {
			return -1
		}
	}
	return result
}