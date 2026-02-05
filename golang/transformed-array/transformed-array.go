package main

import (
	"fmt"
	"reflect"
)

func constructTransformedArray(nums []int) []int {
	n := len(nums)
	result := make([]int, n)

	for i := 0; i < n; i++ {
		target_index := (i + nums[i]) % n

		if target_index < 0 {
			target_index += n
		}

		result[i] = nums[target_index]
	}

	return result
}

func runTest(testNum int, nums []int, expected []int) {
	result := constructTransformedArray(nums)

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
	runTest(1, []int{3, -2, 1, 1}, []int{1, 1, 1, 3})

	// Example 2
	runTest(2, []int{-1, 4, -1}, []int{-1, -1, 4})

	// Zero movement
	runTest(3, []int{0, 0, 0}, []int{0, 0, 0})

	// Full wrap around
	runTest(4, []int{3, 3, 3}, []int{3, 3, 3})
}
