package main

import (
	"fmt"
	"math"
)

func minimumCost(nums []int) int {
	headCost := nums[0]

	min1 := math.MaxInt32
	min2 := math.MaxInt32

	for i := 1; i < len(nums); i++ {
		x := nums[i]
		if x < min1 {
			min2 = min1
			min1 = x
		} else if x < min2 {
			min2 = x
		}
	}

	return headCost + min1 + min2
}

func runTest(testNum int, nums []int, expected int) {
	result := minimumCost(nums)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: %v -> %d (Expected: %d) -> %s\n",
		testNum, nums, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1, []int{1, 2, 3, 12}, 6)

	// Example 2
	runTest(2, []int{5, 4, 3}, 12)

	// Example 3
	runTest(3, []int{10, 3, 1, 1}, 12)
}
