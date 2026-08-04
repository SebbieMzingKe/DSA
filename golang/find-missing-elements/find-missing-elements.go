package main

import (
	"fmt"
	"reflect"
)

func findMissingElements(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}

	minVal := nums[0]
	maxVal := nums[0]
	numSet := make(map[int]struct{}, len(nums))

	for _, num := range nums {
		if num < minVal {
			minVal = num
		}

		if num > maxVal {
			maxVal = num
		}

		numSet[num] = struct{}{}
	}
	missing := make([]int, 0)

	for value := minVal + 1; value < maxVal; value++ {
		if _, exists := numSet[value]; !exists {
			missing = append(missing, value)
		}
	}

	return missing
}

func runTest(testNum int, nums, expected []int) {
	result := findMissingElements(nums)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", testNum)
	fmt.Printf("  Input:    %v\n", nums)
	fmt.Printf("  Output:   %v\n", result)
	fmt.Printf("  Expected: %v\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(1, []int{1, 4, 2, 5}, []int{3})

	// Example 2
	runTest(2, []int{7, 8, 6, 9}, []int{})

	// Example 3
	runTest(3, []int{5, 1}, []int{2, 3, 4})

	// Custom Case: Long gap
	runTest(
		4,
		[]int{10, 20},
		[]int{11, 12, 13, 14, 15, 16, 17, 18, 19},
	)
}
