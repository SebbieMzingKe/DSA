# singly-linked list defn.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        return head


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


def to_array(head):
    """Helper function to convert a Linked List back to a Python list."""
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, arr, expected):
        head = to_linked_list(arr)
        result_head = solver.deleteMiddle(head)
        result_arr = to_array(result_head)

        status = "PASS" if result_arr == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {arr}")
        print(f"  Output:   {result_arr}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1: Odd number of elements
    run_test(1, [1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6])

    # Example 2: Even number of elements
    run_test(2, [1, 2, 3, 4], [1, 2, 4])

    # Example 3: Two elements
    run_test(3, [2, 1], [2])

    # Custom Case 4: Single element (Edge Case)
    run_test(4, [5], [])
