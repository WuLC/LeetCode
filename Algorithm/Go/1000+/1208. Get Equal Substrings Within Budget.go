func equalSubstring(s string, t string, maxCost int) int {
	diff := []int{}
	for i := 0; i < len(s); i++ {
		diff = append(diff, abs(int(s[i])-int(t[i])))
	}
	result, curr, p1, p2 := 0, 0, 0, 0
	for p2 < len(diff) {
		curr += diff[p2]
		if curr <= maxCost {
			result = max(result, p2-p1+1)
		}
		for curr > maxCost {
			curr -= diff[p1]
			p1++
		}
		p2++
	}
	return result
}

func abs(num int) int {
	if num >= 0 {
		return num
	} else {
		return -1 * num
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}