package main

import (
	"fmt"
	"math/bits"
	"reflect"
	"sort"
)

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		bitsI := bits.OnesCount(uint(arr[i]))
		bitsJ := bits.OnesCount(uint(arr[j]))

		if bitsI == bitsJ {
			return arr[i] < arr[j]
		}

		return  bitsI < bitsJ
	})

	return arr
}

func runTest(caseNum int, arr []int, expected []int) {
	input := make([]int, len(arr))
	copy(input, arr)

	result := sortByBits(input)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", caseNum)
	fmt.Printf("  Input:    %v\n", arr)
	fmt.Printf("  Output:   %v\n", result)
	fmt.Printf("  Expected: %v\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	runTest(1,
		[]int{0, 1, 2, 3, 4, 5, 6, 7, 8},
		[]int{0, 1, 2, 4, 8, 3, 5, 6, 7},
	)

	runTest(2,
		[]int{1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1},
		[]int{1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024},
	)

	runTest(3,
		[]int{10, 10, 3, 3},
		[]int{3, 3, 10, 10},
	)

	runTest(4,
		[]int{23, 15},
		[]int{15, 23},
	)
}
