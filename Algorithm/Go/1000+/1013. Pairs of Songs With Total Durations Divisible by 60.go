/*
 * Created on Wed Mar 20 2019 21:29:38
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

func numPairsDivisibleBy60(time []int) int {
	count := [60]int{0}
	for _, t := range time {
		count[t%60]++
	}
	result := 0
	for i := 0; i <= 30; i++ {
		if i == 0 || i == 30 {
			result += (count[i] * (count[i-1])) / 2
		} else {
			result += count[i] * count[60-i]
		}
	}
	return result
}