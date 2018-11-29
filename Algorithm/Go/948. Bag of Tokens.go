/*
 * Created on Thu Nov 29 2018 22:17:45
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy

import (
	"math"
	"sort"
)

func bagOfTokensScore(tokens []int, P int) int {
	sort.Ints(tokens)
	var prefix_sum []int
	curr, result := 0, 0
	for i := 0; i < len(tokens); i++ {
		curr += tokens[i]
		if curr <= P {
			result++
		}
		prefix_sum = append(prefix_sum, curr)
	}

	p1, p2 := 0, len(tokens)-1
	for p1 < p2 {
		if P < tokens[p1] {
			break
		}
		P += tokens[p2] - tokens[p1]
		p1, p2 = p1+1, p2-1
		for i := p2; i > p1-1; i-- {
			if prefix_sum[i]-prefix_sum[p1-1] <= P {
				result = int(math.Max(float64(result), float64(i-p1+1)))
			}
		}
	}
	return result
}