class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """

        def is_possible(time):
            total_time = 0
            needed = time * n

            for battery in batteries:
                total_time += min(battery, time)

                # early exit for optimization
                if total_time > needed:
                    return True
            return total_time >= needed
        
        # ssearch bounds 
        low = 1
        high = sum(batteries) // n

        answer = 0

        while low <= high:
            mid = low + (high - low) // 2

            if is_possible(mid):
                answer = mid
                low = mid + 1
            
            else:
                high = mid - 1
            
        return answer