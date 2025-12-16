class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        total_periods = 1
        current_length = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                current_length += 1
            
            else:
                current_length = 1

            total_periods += current_length

        return total_periods
        
if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1
    prices1 = [3,2,1,4]
    print(f"Test Case 1: {solver.getDescentPeriods(prices1)} (Expected: 7)")
    
    # Test Case 2
    prices2 = [8,6,7,7]
    print(f"Test Case 2: {solver.getDescentPeriods(prices2)} (Expected: 4)")
    
    # Test Case 3
    prices3 = [1]
    print(f"Test Case 3: {solver.getDescentPeriods(prices3)} (Expected: 1)")