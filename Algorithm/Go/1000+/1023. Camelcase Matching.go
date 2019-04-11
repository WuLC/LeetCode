/*
 * Created on Thu Apr 11 2019 21:56:46
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


 // two pointers

import "unicode"

func camelMatch(queries []string, pattern string) []bool {
	result := []bool{}
	for _, q := range queries {
		result = append(result, match([]rune(q), []rune(pattern)))
	}
	return result
}

func match(query, pattern []rune) bool {
	p1, p2 := 0, 0
	n1, n2 := len(query), len(pattern)
	for p1 < n1 && p2 <= n2 {
		if p2 == n2 {
			for p1 < n1 {
				if unicode.IsUpper(query[p1]) {
					return false
				}
				p1++
			}
		} else {
			for p1 < n1 && query[p1] != pattern[p2] {
				if unicode.IsUpper(query[p1]) {
					return false
				}
				p1++
			}
			p1++
			p2++
		}
	}
	return p1 == n1 && p2 == n2
}