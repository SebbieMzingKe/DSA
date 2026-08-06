package main

import (
	"fmt"
	"reflect"
	"sort"
)

func remainingMethods(n int, k int, invocations [][]int) []int {
	// Build adjacency list
	adj := make([][]int, n)
	for _, edge := range invocations {
		u, v := edge[0], edge[1]
		adj[u] = append(adj[u], v)
	}

	// Find all suspicious methods reachable from k
	suspicious := make([]bool, n)
	suspicious[k] = true

	stack := []int{k}

	for len(stack) > 0 {
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		for _, next := range adj[curr] {
			if !suspicious[next] {
				suspicious[next] = true
				stack = append(stack, next)
			}
		}
	}

	// Check if any non-suspicious method invokes a suspicious one
	for _, edge := range invocations {
		u, v := edge[0], edge[1]
		if !suspicious[u] && suspicious[v] {
			result := make([]int, n)
			for i := 0; i < n; i++ {
				result[i] = i
			}
			return result
		}
	}

	// Return all non-suspicious methods
	result := make([]int, 0)
	for i := 0; i < n; i++ {
		if !suspicious[i] {
			result = append(result, i)
		}
	}

	return result
}

func runTest(testNum, n, k int, invocations [][]int, expected []int) {
	result := remainingMethods(n, k, invocations)

	sort.Ints(result)
	sort.Ints(expected)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", testNum)
	fmt.Printf("  Input:    n=%d, k=%d, invocations=%v\n", n, k, invocations)
	fmt.Printf("  Output:   %v\n", result)
	fmt.Printf("  Expected: %v\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(
		1,
		4,
		1,
		[][]int{{1, 2}, {0, 1}, {3, 2}},
		[]int{0, 1, 2, 3},
	)

	// Example 2
	runTest(
		2,
		5,
		0,
		[][]int{{1, 2}, {0, 2}, {0, 1}, {3, 4}},
		[]int{3, 4},
	)

	// Example 3
	runTest(
		3,
		3,
		2,
		[][]int{{1, 2}, {0, 1}, {2, 0}},
		[]int{},
	)

	// Custom Case
	runTest(
		4,
		4,
		2,
		[][]int{{0, 1}},
		[]int{0, 1, 3},
	)
}