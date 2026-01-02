package main

import "fmt"

func repeatedNTimes(nums []int) int {
	seen := make(map[int]bool)

	for _, num := range nums {
		if seen[num] {
			return num
		}
		seen[num] = true
	}

	return -1
}

func main() {
	runTest := func(testNum int, nums []int, expected int) {
		result := repeatedNTimes(nums)
		status := "FAIL"
		if result == expected {
			status = "PASS"
		}
		fmt.Printf("Test Case %d: %d (Expected: %d) -> %s\n", testNum, result, expected, status)
	}

	// Example 1
	nums1 := []int{1, 2, 3, 3}
	runTest(1, nums1, 3)

	// Example 2
	nums2 := []int{2, 1, 2, 5, 3, 2}
	runTest(2, nums2, 2)

	// Example 3
	nums3 := []int{5, 1, 5, 2, 5, 3, 5, 4}
	runTest(3, nums3, 5)
}
