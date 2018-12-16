/*
 * Created on Sat Dec 15 2018 19:37:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two pointers
func isAlienSorted(words []string, order string) bool {
	order_num := make(map[byte]int)
	for i, v := range order {
		order_num[byte(v)] = i
	}

	for i := 0; i < len(words)-1; i++ {
		p1, p2 := 0, 0
		for p1 < len(words[i]) && p2 < len(words[i+1]) {
			if order_num[words[i][p1]] < order_num[words[i+1][p2]] {
				break
			} else if order_num[words[i][p1]] > order_num[words[i+1][p2]] {
				return false
			}
			p1, p2 = p1+1, p2+1
		}
		if p2 == len(words[i+1]) && p1 < len(words[i]) {
			return false
		}
	}
	return true
}