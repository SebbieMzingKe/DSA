class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """     

        n = len(prices)
        half_k = k // 2

        current_total_profit = 0
        original_profit_per_day = [0] * n

        for i in range(n):
            val = strategy[i] * prices[i]
            original_profit_per_day[i] = val
            current_total_profit += val

            prefix_prices = [0] * (n + 1)
            prefix_orig_profit = [0] * (n + 1)

        for i in range(n):
            prefix_prices[i + 1] = prefix_prices[i] + prices[i]
            prefix_orig_profit[i + 1] = prefix_orig_profit[i] + original_profit_per_day[i]

            max_diff = 0

        
        for i in range(n - k + 1):
            old_window_profit = prefix_orig_profit[i + k] - prefix_orig_profit[i]

            new_window_profit = prefix_prices[i + k] - prefix_prices[i + half_k]
            diff = new_window_profit - old_window_profit

            if diff > max_diff:
                max_diff = diff
        return current_total_profit + max_diff
    

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    prices1 = [4, 2, 8]
    strategy1 = [-1, 0, 1]
    k1 = 2
    print(f"Test Case 1: {solver.maxProfit(prices1, strategy1, k1)} (Expected: 10)")

    # Test Case 2
    prices2 = [5, 4, 3]
    strategy2 = [1, 1, 0]
    k2 = 2
    print(f"Test Case 2: {solver.maxProfit(prices2, strategy2, k2)} (Expected: 9)")