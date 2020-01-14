/*
 * Created on Mon Jan 13 2020 10:17:54
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

/*
 * Created on Mon Jan 13 2020 10:17:54
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 func makeConnected(n int, connections [][]int) int {
	if len(connections) < n - 1 {
		return -1
	}
	graph := make(map[int][]int)
	for _, k := range connections {
		graph[k[0]] = append(graph[k[0]], k[1])
		graph[k[1]] = append(graph[k[1]], k[0])
	}
    visited := []int{}
    for i := 0; i < n; i++ {
        visited = append(visited, 0)
    }
	result := 0
	for i:= 0; i < n; i++ {
		result += dfs(i, graph, visited)
	}
	return result - 1
}

func dfs(i int, graph map[int][]int, visited []int) int {
	if visited[i] == 1 {
		return 0
	}
	visited[i] = 1
	for _, v := range graph[i] {
		if visited[v] == 1 {
			continue
		}
		dfs(v, graph, visited)
	}
	return 1
}