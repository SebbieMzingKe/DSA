package main

import (
	"fmt"
	"math"
	"sort"
)

func minimumDifference(nums []int, k int) int {
	if k == 1 {
		return 0
	}

	sort.Ints(nums)

	minDiff := math.MaxInt32

	for i := 0; i <= len(nums)-k; i++ {
		currentDiff := nums[i+k-1] - nums[i]
		if currentDiff < minDiff {
			minDiff = currentDiff
		}
	}

	return minDiff
}

func runTest(testNum int, nums []int, k int, expected int) {
	input := make([]int, len(nums))
	copy(input, nums)

	result := minimumDifference(input, k)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: nums=%v, k=%d -> %d (Expected: %d) -> %s\n",
		testNum, nums, k, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1, []int{90}, 1, 0)

	// Example 2
	runTest(2, []int{9, 4, 1, 7}, 2, 2)

	// Custom Case
	runTest(3, []int{1, 5, 10}, 3, 9)
}
