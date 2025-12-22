class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        R = len(strs)
        C = len(strs[0])

        delete_count = 0

        for  col in range(C):
            for row in range(R - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete_count += 1
                    break

        return delete_count
    
if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Grid:
    # c b a
    # d a f
    # g h i
    # Col 0: c < d < g (Sorted)
    # Col 1: b > a (Not Sorted -> Delete)
    # Col 2: a < f < i (Sorted)
    print(f"Test Case 1: {solver.minDeletionSize(['cba','daf','ghi'])} (Expected: 1)")
    
    # Example 2
    print(f"Test Case 2: {solver.minDeletionSize(['a','b'])} (Expected: 0)")
    
    # Example 3
    print(f"Test Case 3: {solver.minDeletionSize(['zyx','wvu','tsr'])} (Expected: 3)")