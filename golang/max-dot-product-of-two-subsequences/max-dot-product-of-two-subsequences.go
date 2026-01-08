package main

import (
	"fmt"
	"math"
)

func maxDotProduct(nums1 []int, nums2 []int) int {
	n, m := len(nums1), len(nums2)

	dp := make([][]int, n+1)

	for i := range dp {
		dp[i] = make([]int, m+1)
		for j := range dp[i] {
			dp[i][j] = math.MinInt32
		}
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			current := nums1[i-1] * nums2[j-1]

			include := current
			if dp[i-1][j-1] > 0 {
				include += dp[i-1][j-1]
			}

			skipI := dp[i-1][j]
			skipJ := dp[i][j-1]

			dp[i][j] = max(include, skipI, skipJ)
		}
	}

	return dp[n][m]
}

func max(a, b, c int) int {
	if a >= b && a >= c {
		return a
	}

	if b >= a && b >= c {
		return b
	}

	return c
}

func runTest(testNum int, nums1, nums2 []int, expected int) {
	result := maxDotProduct(nums1, nums2)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d: %d (Expected: %d) -> %s\n",
		testNum, result, expected, status)
}

func main() {
	// Example 1
	runTest(1,
		[]int{2, 1, -2, 5},
		[]int{3, 0, -6},
		18,
	)

	// Example 2
	runTest(2,
		[]int{3, -2},
		[]int{2, -6, 7},
		21,
	)

	// Example 3 (Negative result required)
	runTest(3,
		[]int{-1, -1},
		[]int{1, 1},
		-1,
	)

	// Edge Case: Single elements
	runTest(4,
		[]int{-5},
		[]int{5},
		-25,
	)

	// Edge Case: Zeros
	runTest(5,
		[]int{0, 0},
		[]int{1, -5},
		0,
	)
}
