# singly-linked list definition
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        max_sum = 0
        first_half = head
        second_half = prev

        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return max_sum


def to_linked_list(arr):
    """Helper function to convert a Python list to a Linked List."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, arr, expected):
        head = to_linked_list(arr)
        result = solver.pairSum(head)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {arr}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [5, 4, 2, 1], 6)

    # Example 2
    run_test(2, [4, 2, 2, 3], 7)

    # Example 3
    run_test(3, [1, 100000], 100001)

    # Custom Case 4: Longer list
    run_test(4, [1, 2, 3, 4, 5, 6, 7, 8], 9)
