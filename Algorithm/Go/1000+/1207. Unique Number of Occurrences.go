func uniqueOccurrences(arr []int) bool {
	counter := make(map[int]int)
	for _, num := range arr {
		counter[num]++
	}
	unique := make(map[int]bool)
	for _, v := range counter {
		if unique[v] {
			return false
		}
		unique[v] = true
	}
	return true
}