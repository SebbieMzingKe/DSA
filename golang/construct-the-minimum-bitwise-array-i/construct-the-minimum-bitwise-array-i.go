package main

import (
	"fmt"
	"reflect"
)

func minBitwiseArray(nums []int) []int {
	ans := make([]int, 0, len(nums))

	for _, n := range nums {
		found := false

		for x := 0; x < n; x++ {
			if (x | (x + 1)) == n {
				ans = append(ans, x)

				found = true
				break
			}
		}
		if !found {
			ans = append(ans, -1)
		}
	}

	return ans
}

func runTest(testNum int, nums []int, expected []int) {
	result := minBitwiseArray(nums)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: Input %v -> Output %v (Expected: %v) -> %s\n",
		testNum, nums, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1,
		[]int{2, 3, 5, 7},
		[]int{-1, 1, 4, 3},
	)

	// Example 2
	runTest(2,
		[]int{11, 13, 31},
		[]int{9, 12, 15},
	)

	// Edge Case
	runTest(3,
		[]int{2},
		[]int{-1},
	)
}
