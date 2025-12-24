class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        boxes_used = 0
        current_capacity = 0
        
        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            
            if current_capacity >= total_apples:
                return boxes_used
                
        return boxes_used

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    apple1 = [1, 3, 2]
    capacity1 = [4, 3, 1, 5, 2]
    result1 = solver.minimumBoxes(apple1, capacity1)
    print(f"Test Case 1: Input: apple={apple1}, capacity={capacity1}")
    print(f"Result: {result1} | Expected: 2\n")

    # Test Case 2
    apple2 = [5, 5, 5]
    capacity2 = [2, 4, 2, 7]
    result2 = solver.minimumBoxes(apple2, capacity2)
    print(f"Test Case 2: Input: apple={apple2}, capacity={capacity2}")
    print(f"Result: {result2} | Expected: 4\n")