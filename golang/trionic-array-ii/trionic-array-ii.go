package main

import (
	"fmt"
	"math"
)

func maxSumTrionic(nums []int) int64 {
	n := len(nums)
	if n < 3 {
		return 0
	}

	var inc1 int64 = math.MinInt64 / 2
	var dec int64 = math.MinInt64 / 2
	var inc2 int64 = math.MinInt64 / 2
	var maxSum int64 = math.MinInt64 / 2

	for i := 1; i < n; i++ {
		curr := int64(nums[i])
		prev := int64(nums[i-1])

		var nextInc1 int64 = math.MinInt64 / 2
		var nextDec int64 = math.MinInt64 / 2
		var nextInc2 int64 = math.MinInt64 / 2

		if curr > prev {
			nextInc1 = maxInt64(prev, inc1) + curr
			nextInc2 = maxInt64(inc2, dec) + curr
		} else if curr < prev {
			nextDec = maxInt64(dec, inc1) + curr
		}

		inc1 = nextInc1
		dec = nextDec
		inc2 = nextInc2

		if inc2 > maxSum {
			maxSum = inc2
		}
	}

	if maxSum < -1e15 {
		return 0
	}

	return maxSum
}


func maxInt64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func runTest(testNum int, nums []int, expected int) {
	result := maxSumTrionic(nums)
	status := "FAIL"
	if result == int64(expected) {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: %d (Expected: %d) -> %s\n",
		testNum, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1, []int{0, -2, -1, -3, 0, 2, -1}, -4)

	// Example 2
	runTest(2, []int{1, 4, 2, 7}, 14)

	// Custom Case: Negative domination
	runTest(3, []int{-5, -1, -5, -1}, -12)

	// Simple valid case
	runTest(4, []int{1, 5, 2, 6}, 14)
}
