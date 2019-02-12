/*
 * Created on Sun Feb 10 2019 15:27:20
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

type UnionFindSet struct {
	parent []int
	rank []int
}

func(ufs *UnionFindSet) find(v int) int {
	if ufs.parent[v] != v {
		ufs.parent[v] = ufs.find(ufs.parent[v])
	}
	return ufs.parent[v]
}

func(ufs *UnionFindSet) union(v1, v2 int) {
	p1, p2 := ufs.find(v1), ufs.find(v2)
	if ufs.rank[p1] > ufs.rank[p2] {
		ufs.parent[p2] = p1
	} else if ufs.rank[p1] < ufs.rank[p2] {
		ufs.parent[p1] = p2
	} else {
		ufs.parent[p2] = p1
		ufs.rank[p1]++		
	}
}


func equationsPossible(equations []string) bool {
	ufs := UnionFindSet{[]int{}, []int{}}
	for i := 0; i < 26; i++ {
		ufs.parent = append(ufs.parent, i)
		ufs.rank = append(ufs.rank, 0)
	}

	for _, e := range equations {
		if int(e[1]) == 61 {
			ufs.union(int(e[0]) - 97, int(e[3]) - 97)
		}
	}

	for _, e := range equations {
		if int(e[1]) != 61 && ufs.find(int(e[0]) - 97) == ufs.find(int(e[3]) - 97) {
			return false
		}
	}
	return true
}