package main

import (
	"fmt"
	"reflect"
	"sort"
)

func minRemoval(nums []int, k int) int{
	sort.Ints((nums))

	n := len(nums)

	maxKept := 0
	left := 0

	for right := 0; right < n; right++ {
		for nums[right] > nums[left] * k {
			left++
		}

		windowSize := right - left + 1
		if windowSize > maxKept {
			maxKept = windowSize
		}
	}

	return  n - maxKept
}

func runTest(testNum int, nums []int, k int, expected int) {
	numsCopy := make([]int, len(nums))
	copy(numsCopy, nums)

	result := minRemoval(numsCopy, k)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: %v, k=%d -> %d (Expected: %d) -> %s\n",
		testNum, nums, k, result, expected, status,
	)
}

func main() {
	runTest(1, []int{2, 1, 5}, 2, 1)
	runTest(2, []int{1, 6, 2, 9}, 3, 2)
	runTest(3, []int{4, 6}, 2, 0)
	runTest(4, []int{5, 5, 5}, 1, 0)
}