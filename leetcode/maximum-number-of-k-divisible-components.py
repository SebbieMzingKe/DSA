from collections import defaultdict


class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """

        adjacency = defaultdict(list)

        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        result = [0]

        def dfs(current_node, parent):
            total = values[current_node]

            for child in adjacency[current_node]:
                if child != parent:
                    total = dfs(child, current_node)
                    if total % k == 0:
                        result[0] += 1
                        return 0
                    return total
            
            dfs(0, -1)
            return result[0]