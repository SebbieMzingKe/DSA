class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """

        happiness.sort(reverse = True)

        total_happiness = 0

        for i in range(k):
            
            current_value = max(happiness[i] - i, 0) 

            if current_value == 0:
                break

            total_happiness += current_value

        return total_happiness


if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Sort: [3, 2, 1]. 
    # Pick 3 (turn 0, penalty 0) -> 3
    # Pick 2 (turn 1, penalty 1) -> 1
    # Total: 4
    h1 = [1, 2, 3]
    k1 = 2
    print(f"Test Case 1: {solver.maximumHappinessSum(h1, k1)} (Expected: 4)")
    
    # Example 2
    # Sort: [1, 1, 1, 1].
    # Pick 1 (turn 0, penalty 0) -> 1
    # Pick 1 (turn 1, penalty 1) -> 0
    # Total: 1
    h2 = [1, 1, 1, 1]
    k2 = 2
    print(f"Test Case 2: {solver.maximumHappinessSum(h2, k2)} (Expected: 1)")
    
    # Example 3
    # Sort: [5, 4, 3, 2].
    # Pick 5 (turn 0, penalty 0) -> 5
    # Total: 5
    h3 = [2, 3, 4, 5]
    k3 = 1
    print(f"Test Case 3: {solver.maximumHappinessSum(h3, k3)} (Expected: 5)")