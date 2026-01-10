package main

import "fmt"

// defn of binary tree node

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	var dfs func(node *TreeNode) (*TreeNode, int)

	dfs = func(node *TreeNode) (*TreeNode, int) {
		if node == nil {
			return nil, 0
		}

		leftNode, leftDepth := dfs(node.Left)
		rightNode, rightDepth := dfs(node.Right)

		if leftDepth > rightDepth {
			return leftNode, leftDepth + 1
		}

		if rightDepth > leftDepth {
			return rightNode, rightDepth + 1
		}

		return node, leftDepth + 1
	}

	result, _ := dfs(root)
	return result
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

func runTest(testNum int, values []*int, expectedVal int) {
	root := buildTree(values)
	result := subtreeWithAllDeepest(root)

	resultVal := -1
	if result != nil {
		resultVal = result.Val
	}

	status := "FAIL"
	if resultVal == expectedVal {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: Output Node Val = %d (Expected: %d) -> %s\n",
		testNum, resultVal, expectedVal, status,
	)
}

func main() {
	ptr := func(v int) *int { return &v }

	// Example 1
	runTest(1,
		[]*int{
			ptr(3), ptr(5), ptr(1), ptr(6), ptr(2), ptr(0), ptr(8),
			nil, nil, ptr(7), ptr(4),
		},
		2,
	)

	// Example 2
	runTest(2,
		[]*int{ptr(1)},
		1,
	)

	// Example 3
	runTest(3,
		[]*int{ptr(0), ptr(1), ptr(3), nil, ptr(2)},
		2,
	)
}
