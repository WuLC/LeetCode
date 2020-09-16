// greedy, O(m+n) time

func isTransformable(s string, t string) bool {
	idx := make(map[int][]int)
	for i, char := range s {
		val := int(char - '0')
		idx[val] = append(idx[val], i)
	}
	counter := make(map[int]int)
	for _, char := range t {
		val := int(char - '0')
		if counter[val] >= len(idx[val]) {
			return false
		}
		for i = 0; i < val; i++ {
			if counter[i] < len(idx[i]) && idx[i][counter[i]] < idx[val][counter[val]] {
				return false
			}
		}
		counter[val]++
	}
	return true
}