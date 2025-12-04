class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        n = len(directions)
        l, r = 0, n - 1

        while l < n and directions == 'L':
            l += 1
        
        while r >= 0 and directions == 'R':
            r -= 1

        if l > r:
            return 0

        answer = 0
        for i in range(l, r + 1):
            if directions[i] != 'S':
                answer += 1
        
        return answer