/*
 * Created on Thu Jan 17 2019 9:52:7
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// implement the priority queue in golang
// refer: https://golang.org/pkg/container/heap/
import "container/heap"

// An Item is something we manage in a priority queue.
type Item struct {
	value    []int // The value of the item; arbitrary.
	priority int   // The priority of the item in the queue.
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest instead of lowest priority so we use greater than here.
	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func kClosest(points [][]int, K int) [][]int {
	pq := make(PriorityQueue, K)
	i := 0
	for i < K {
		p := points[i]
		pq[i] = &Item{
			value:    p,
			priority: p[0]*p[0] + p[1]*p[1],
			index:    i,
		}
		i++
	}
	heap.Init(&pq)
	for i < len(points) {
		p := points[i]
		heap.Push(&pq, &Item{
			value:    p,
			priority: p[0]*p[0] + p[1]*p[1],
		})
		heap.Pop(&pq)
		i++
	}
	result := [][]int{}
	for _, item := range pq {
		result = append(result, (*item).value)
	}
	return result
}