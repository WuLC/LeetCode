func minReorder(n int, connections [][]int) int {
	// build index
	neighbor, direction := make(map[int]map[int]bool), make(map[int]map[int]bool)
	for _, conn := range connections {
		if _, exist := neighbor[conn[0]]; !exist {
			neighbor[conn[0]] = make(map[int]bool)
		}
		if _, exist := neighbor[conn[1]]; !exist {
			neighbor[conn[1]] = make(map[int]bool)
		}
		if _, exist := direction[conn[0]]; !exist {
			direction[conn[0]] = make(map[int]bool)
		}
		neighbor[conn[0]][conn[1]] = true
		neighbor[conn[1]][conn[0]] = true
		direction[conn[0]][conn[1]] = true
	}
	// bfs
	result := 0
	queue, visited := []int{0}, make(map[int]bool)
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		for node, _ := range neighbor[curr] {
			if _, exist := visited[node]; exist {
				continue
			}
			visited[curr] = true
			if _, exist := direction[node]; !exist {
				result++
			} else {
				if _, exist := direction[node][curr]; !exist {
					result++
				}
			}
			queue = append(queue, node)
		}
	}
	return result
}