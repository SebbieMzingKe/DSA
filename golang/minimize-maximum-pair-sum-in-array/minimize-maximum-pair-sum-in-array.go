package main

import (
	"fmt"
	"sort"
)

func minPairSum(nums []int) int {
	sort.Ints(nums)

	n := len(nums)
	maxPairSum := 0

	for i := 0; i < n/2; i++ {
		currentSum := nums[i] + nums[n-1-i]
		if currentSum > maxPairSum {
			maxPairSum = currentSum
		}
	}

	return maxPairSum
}

func runTest(testNum int, nums []int, expected int) {
	// copy because sorting mutates the slice
	input := make([]int, len(nums))
	copy(input, nums)

	result := minPairSum(input)

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
	runTest(1, []int{3, 5, 2, 3}, 7)

	// Example 2
	runTest(2, []int{3, 5, 4, 2, 4, 6}, 8)

	// Custom Case
	runTest(3, []int{1, 10, 2, 9}, 11)
}
