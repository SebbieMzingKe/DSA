package main

import (
	"fmt"
	"math"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	maxSum := math.MinInt64
	maxLevel := 1
	currentLevel := 1

	queue := []*TreeNode{root}

	for len(queue) > 0 {
		levelSum := 0
		size := len(queue)

		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]

			levelSum += node.Val

			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		if levelSum > maxSum {
			maxSum = levelSum
			maxLevel = currentLevel
		}

		currentLevel++
	}

	return maxLevel
}

func buildTree(values []*int) *TreeNode {
	if len(values) == 0 || values[0] == nil {
		return nil
	}

	root := &TreeNode{Val: *values[0]}
	queue := []*TreeNode{root}

	i := 1

	for len(queue) > 0 && i < len(values) {
		node := queue[0]
		queue = queue[1:]

		if i < len(values) && values[i] != nil {
			node.Left = &TreeNode{Val: *values[i]}
			queue = append(queue, node.Left)
		}

		i++

		if i < len(values) && values[i] != nil {
			node.Right = &TreeNode{Val: *values[i]}
			queue = append(queue, node.Right)
		}

		i++
	}

	return root
}

func runTest(testNum int, values []*int, expected int) {
	root := buildTree(values)
	result := maxLevelSum(root)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d: %d (Expected: %d) -> %s\n",
		testNum, result, expected, status)
}

func main() {
	ptr := func(v int) *int { return &v }

	// Example 1
	runTest(1,
		[]*int{ptr(1), ptr(7), ptr(0), ptr(7), ptr(-8), nil, nil},
		2,
	)

	// Example 2
	runTest(2,
		[]*int{ptr(989), nil, ptr(10250), ptr(98693), ptr(-89388), nil, nil, nil, ptr(-32127)},
		2,
	)

	// Edge Case: All negative
	runTest(3,
		[]*int{ptr(-100), ptr(-200), ptr(-300)},
		1,
	)
}
