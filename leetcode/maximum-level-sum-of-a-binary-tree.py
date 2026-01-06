# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        queue = deque([root])

        while queue:
            level_sum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level
    
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while deque and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1
    
    return root
    

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, values, expected):
        root = build_tree(values)
        result = solver.maxLevelSum(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Level 1: 1
    # Level 2: 7 + 0 = 7 (Max)
    # Level 3: 7 - 8 = -1
    run_test(1, [1, 7, 0, 7, -8, None, None], 2)
    
    # Example 2
    # Level 1: 989
    # Level 2: 10250 (Max)
    # Level 3: 98693 - 89388 = 9305
    # Level 4: -32127
    run_test(2, [989, None, 10250, 98693, -89388, None, None, None, -32127], 2)

    # Edge Case: All negative numbers
    # Level 1: -100 (Max)
    # Level 2: -200 - 300 = -500
    run_test(3, [-100, -200, -300], 1)