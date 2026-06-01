package main

import (
	"fmt"
	"sort"
)

func minimumCost(cost []int) int {
	// Sort the slice in descending order
	sort.Slice(cost, func(i, j int) bool {
		return cost[i] > cost[j]
	})

	totalCost := 0
	for i := 0; i < len(cost); i++ {
		if (i+1)%3 != 0 {
			totalCost += cost[i]
		}
	}
	return totalCost
}

func runTest(caseNum int, cost []int, expected int) {
	// Copy cost so printing displays the original un-mutated list
	costCopy := make([]int, len(cost))
	copy(costCopy, cost)

	result := minimumCost(costCopy)
	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", caseNum)
	fmt.Printf("  Input costs: %v\n", cost)
	fmt.Printf("  Output:      %d\n", result)
	fmt.Printf("  Expected:    %d\n", expected)
	fmt.Printf("  Status:      %s\n\n", status)
}

func main() {
	runTest(1, []int{1, 2, 3}, 5)
	runTest(2, []int{6, 5, 7, 9, 2, 2}, 23)
	runTest(3, []int{5, 5}, 10)
	runTest(4, []int{10, 10, 10}, 20)
}
