class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        
        # Coordinate Compression
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        sorted_xs = sorted(list(xs))
        x_map = {val: i for i, val in enumerate(sorted_xs)}
        n_unique = len(sorted_xs)

        # type 1 for entering a square, -1 for leaving
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        # Sort by y.
        events.sort(key=lambda x: x[0])

        # 3. Segment Tree Arrays
        self.tree_cnt = [0] * (4 * n_unique)
        self.tree_len = [0.0] * (4 * n_unique)
        self.sorted_xs = sorted_xs

        # 4. Helper for Segment Tree
        def update(node, start, end, q_l, q_r, val):
            if q_l <= start and end <= q_r:
                self.tree_cnt[node] += val
            else:
                mid = (start + end) // 2
                if q_l < mid:
                    update(2 * node, start, mid, q_l, q_r, val)
                if q_r > mid:
                    update(2 * node + 1, mid, end, q_l, q_r, val)
            
            # Push Up Logic
            if self.tree_cnt[node] > 0:
                self.tree_len[node] = self.sorted_xs[end] - self.sorted_xs[start]
            elif end - start == 1:
                # Leaf not covered
                self.tree_len[node] = 0
            else:
                # Internal node partially covered
                self.tree_len[node] = self.tree_len[2 * node] + self.tree_len[2 * node + 1]

        # sweep line
        history = []
        prev_y = events[0][0]
        
        i = 0
        n_events = len(events)
        
        while i < n_events:
            curr_y = events[i][0]
            
            if curr_y > prev_y:
                active_len = self.tree_len[1] # root holds the total active length
                history.append((prev_y, curr_y, active_len))
            
            # Process all events at this exact y-coordinate
            while i < n_events and events[i][0] == curr_y:
                _, type_, x1, x2 = events[i]
                l_idx, r_idx = x_map[x1], x_map[x2]
                # Update range [l_idx, r_idx)
                update(1, 0, n_unique - 1, l_idx, r_idx, type_)
                i += 1
            
            prev_y = curr_y

        # 6. calculate total and find split
        total_area = sum((end - start) * length for start, end, length in history)
        target = total_area / 2.0
        
        current_area = 0.0
        for start, end, length in history:
            segment_area = (end - start) * length
            
            if current_area + segment_area >= target:
                needed = target - current_area
                # height = Area / width
                if length == 0: 
                    return float(start)
                return start + needed / length
                
            current_area += segment_area
            
        return float(prev_y)

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, squares, expected):
        result = solver.separateSquares(squares)
        diff = abs(result - expected)
        status = "PASS" if diff < 1e-5 else "FAIL"
        print(f"Test Case {case_num}: Result {result:.5f} (Expected: {expected:.5f}) -> {status}")

    # Example 1
    # Squares separate. Area 2. Cut at 1.0.
    run_test(1, [[0,0,1],[2,2,1]], 1.00000)

    # Example 2
    # Overlapping squares. 
    # Sq1 (Blue): [0,0,2] -> Covers x[0,2], y[0,2]
    # Sq2 (Red):  [1,1,1] -> Covers x[1,2], y[1,2]
    # Total Union Area:
    # y[0,1]: covers x[0,2] (len 2). Area = 1*2 = 2.
    # y[1,2]: covers x[0,2] (Union of [0,2] and [1,2] is [0,2]). Length 2. Area = 1*2 = 2.
    # Total = 4. Target = 2.
    # Cut happens exactly after the first strip (y=1).
    run_test(2, [[0,0,2],[1,1,1]], 1.00000)
    
    # Custom Case: Complex Overlap
    # Two identical squares [0,0,2] and [0,0,2].
    # Union Area is just area of one square = 4. Target = 2.
    # Cut at y=1.
    run_test(3, [[0,0,2],[0,0,2]], 1.00000)