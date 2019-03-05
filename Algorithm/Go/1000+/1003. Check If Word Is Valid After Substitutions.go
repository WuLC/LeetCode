/*
 * Created on Tue Mar 05 2019 18:1:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// iterate from left to right, there should always be #a>#b>#c
func isValid(S string) bool {
	counter := make(map[rune]int)
	for _, c := range S {
		counter[c]++
		if !(counter['a'] >= counter['b'] && counter['b'] >= counter['c']) {
			return false
		}
	}
	if counter['a'] == counter['b'] && counter['b'] == counter['c'] {
		return true
	} else {
		return false
	}
}