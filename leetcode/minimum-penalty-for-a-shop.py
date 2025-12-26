class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        # Initial penalty at hour 0 = Total 'Y's
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        best_hour = 0
        
        for i, char in enumerate(customers):
            # Transition from closing at hour i to closing at hour i+1
            if char == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1
            
            # Update minimum if we found a strictly smaller penalty
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1
                
        return best_hour

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    # Y Y N Y
    # 0: Close 0 -> Miss 3 Ys -> Penalty 3
    # 1: Close 1 -> Open(Y), Close(YNY) -> Penalty 0 + 2 = 2
    # 2: Close 2 -> Open(YY), Close(NY) -> Penalty 0 + 1 = 1 (Best)
    # 3: Close 3 -> Open(YYN), Close(Y) -> Penalty 1 + 1 = 2
    # 4: Close 4 -> Open(YYNY), Close() -> Penalty 1 + 0 = 1 (Not earlier than 2)
    s1 = "YYNY"
    print(f"Test Case 1: {solver.bestClosingTime(s1)} (Expected: 2)")
    
    # Example 2
    # N N N N N
    # Close at 0 is best (Penalty 0). Opening incurs penalties for Ns.
    s2 = "NNNNN"
    print(f"Test Case 2: {solver.bestClosingTime(s2)} (Expected: 0)")
    
    # Example 3
    # Y Y Y Y
    # Close at 4 is best. Every hour open satisfies a customer.
    s3 = "YYYY"
    print(f"Test Case 3: {solver.bestClosingTime(s3)} (Expected: 4)")