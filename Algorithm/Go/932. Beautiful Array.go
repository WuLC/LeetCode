func beautifulArray(N int) []int {
	result := []int{1}
	for len(result) < N {
		odds, evens := []int{}, []int{}
		for _, num := range result {
			if num*2-1 <= N {
				odds = append(odds, num*2-1)
			}
			if num*2 <= N {
				evens = append(evens, num*2)
			}
		}
		odds = append(odds, evens...)
		result = odds
	}
	return result
}