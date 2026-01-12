package main

import "fmt"

func minTimeToVisitAllPoints(points [][]int) int {
	totalTime := 0

	for i := 1; i < len(points); i++ {
		prev := points[i-1]
		curr := points[i]

		dx := abs(curr[0] - prev[0])
		dy := abs(curr[1] - prev[1])

		if dx > dy {
			totalTime += dx
		} else {
			totalTime += dy
		}
	}

	return totalTime
}

func abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func runTest(testNum int, points [][]int, expected int) {
	result := minTimeToVisitAllPoints(points)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: %v -> %d (Expected: %d) -> %s\n",
		testNum, points, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1,
		[][]int{{1, 1}, {3, 4}, {-1, 0}},
		7,
	)

	// Example 2
	runTest(2,
		[][]int{{3, 2}, {-2, 2}},
		5,
	)

	// Edge Case: Diagonal move
	runTest(3,
		[][]int{{0, 0}, {2, 2}},
		2,
	)

	// Edge Case: Vertical move
	runTest(4,
		[][]int{{0, 0}, {0, 5}},
		5,
	)
}
