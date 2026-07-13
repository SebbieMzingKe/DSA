package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	var prev *ListNode
	curr := slow

	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}

	maxSum := 0
	firstHalf := head
	secondHalf := prev

	for secondHalf != nil {
		sum := firstHalf.Val + secondHalf.Val
		if sum > maxSum {
			maxSum = sum
		}

		firstHalf = firstHalf.Next
		secondHalf = secondHalf.Next
	}

	return maxSum
}

func buildLinkedList(values []int) *ListNode {
	if len(values) == 0 {
		return nil
	}

	head := &ListNode{Val: values[0]}
	curr := head

	for _, value := range values[1:] {
		curr.Next = &ListNode{Val: value}
		curr = curr.Next
	}

	return head
}

func runTest(testNum int, values []int, expected int) {
	head := buildLinkedList(values)
	result := pairSum(head)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: %v -> %d (Expected: %d) -> %s\n",
		testNum, values, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1, []int{5, 4, 2, 1}, 6)

	// Example 2
	runTest(2, []int{4, 2, 2, 3}, 7)

	// Example 3
	runTest(3, []int{1, 100000}, 100001)

	// Custom Case 4: Longer list
	runTest(4, []int{1, 2, 3, 4, 5, 6, 7, 8}, 9)
}
