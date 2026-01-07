# Definition for a binary tree node.
from collections import deque
from platform import node


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        all_sums = []

        def get_sum(node):
            if not node:
                return 0
            

            current_sum = node.val + get_sum(node.left) + get_sum(node.right)
            all_sums.append(current_sum)
            return current_sum

        total_sum = get_sum(root)

        best_product  = 0

        for s in all_sums:
            product = s * (total_sum - s)
            best_product = max(best_product, product)

        return best_product % (10**9 + 7)


def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])

    i = 1
    while queue and i < len(values):
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
        result = solver.maxProduct(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Tree: [1,2,3,4,5,6] -> Total Sum = 21
    # Possible cuts:
    # Cut below 2 (Subtree sum 11: 2+4+5): 11 * (21-11) = 110
    # Cut below 3 (Subtree sum 9: 3+6): 9 * (21-9) = 108
    run_test(1, [1, 2, 3, 4, 5, 6], 110)
    
    # Example 2
    # Tree: [1,null,2,3,4,null,null,5,6] -> Total Sum = 21
    # Subtree at 2 (Sum 6: 2+4): 6 * 15 = 90
    run_test(2, [1, None, 2, 3, 4, None, None, 5, 6], 90)