package main

import "fmt"

func maximumMinutes(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dirs := []int{0, 1, 0, -1, 0}

	// precompute fire arrival times.
	fireTime := make([][]int, m)
	for i := range fireTime {
		fireTime[i] = make([]int, n)
		for j := range fireTime[i] {
			fireTime[i][j] = -1 // unvisited
		}
	}

	fireQueue := [][2]int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				fireQueue = append(fireQueue, [2]int{i, j})
				fireTime[i][j] = 0
			}
		}
	}

	// bfs for fire
	qIdx := 0
	for qIdx < len(fireQueue) {
		current := fireQueue[qIdx]
		qIdx++

		r, c := current[0], current[1]
		t := fireTime[r][c]

		for k := 0; k < 4; k++ {
			nr, nc := r+dirs[k], c+dirs[k+1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 2 && fireTime[nr][nc] == -1 {
				fireTime[nr][nc] = t + 1
				fireQueue = append(fireQueue, [2]int{nr, nc})
			}
		}
	}

	// check feasibility
	canReach := func(waitTime int) bool {

		// fire is at start
		if fireTime[0][0] != -1 && fireTime[0][0] <= waitTime {
			return false
		}

		visited := make([][]bool, m)

		for i := range visited {
			visited[i] = make([]bool, n)
		}

		pq := [][2]int{{0, 0}}
		visited[0][0] = true
		currentTime := waitTime

		// bfs to track time
		for len(pq) > 0 {
			sz := len(pq)
			currentTime++ // arriving at the next cells.

			for i := 0; i < sz; i++ {
				current := pq[0]
				pq = pq[1:]
				r, c := current[0], current[1]

				for k := 0; k < 4; k++ {
					nr, nc := r+dirs[k], c+dirs[k+1]

					if nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && grid[nr][nc] != 2 {
						fTime := fireTime[nr][nc]

						if nr == m-1 && nc == n-1 {
							// safehouse
							if fTime == -1 || currentTime <= fTime {
								return true
							}
						} else {
							// normal cell
							if fTime == -1 || currentTime < fTime {
								visited[nr][nc] = true
								pq = append(pq, [2]int{nr, nc})

							}
						}
					}
				}
			}
		}
		return false
	}

	// binary search for the max waitTime
	low, high := 0, 1000000000
	answer := -1

	for low <= high {
		mid := low + (high-low)/2

		if canReach(mid) {
			answer = mid
			low = mid + 1

		} else {
			high = mid - 1
		}
	}

	return answer
}

func main() {
	runTest := func(testNum int, grid [][]int, expected int) {
		result := maximumMinutes(grid)

		status := "FAIL"
		if result == expected {
			status = "PASS"
		}
		fmt.Printf("test case %d: %d (expected: %d) -> %s\n", testNum, result, expected, status)
	}

	grid1 := [][]int{
		{0, 2, 0, 0, 0, 0, 0},
		{0, 0, 0, 2, 2, 1, 0},
		{0, 2, 0, 0, 1, 2, 0},
		{0, 0, 2, 2, 2, 0, 2},
		{0, 0, 0, 0, 0, 0, 0},
	}
	runTest(1, grid1, 3)

	// Example 2 (Immediate fire danger)
	grid2 := [][]int{
		{0, 0, 0, 0},
		{0, 1, 2, 0},
		{0, 2, 0, 0},
	}
	runTest(2, grid2, -1)

	// Example 3 (Safe forever)
	grid3 := [][]int{
		{0, 0, 0},
		{2, 2, 0},
		{1, 2, 0},
	}
	runTest(3, grid3, 1000000000)
}
